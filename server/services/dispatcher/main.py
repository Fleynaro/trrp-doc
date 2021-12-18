from os import listdir
from concurrent import futures
import grpc

from dispatcher_pb2 import DocumentInfoResponse, DocServer, AddDocServerResponse
from document_pb2 import PingRequest
import dispatcher_pb2_grpc
import document_pb2_grpc

from config import CFG
from utils import title_to_id



class DispatcherService(
    dispatcher_pb2_grpc.DispatcherServiceServicer):
    """сервис по работе со множеством документов
    """
    def __init__(self):
        super().__init__()
        self.doc_servers = []

    def GetDocuments(self, request, context):
        """получение списка документов
        """
        doc_dir = CFG['storage']['dir']
        for title in listdir(doc_dir):
            yield DocumentInfoResponse(
                docId=title_to_id(title),
                title=title)
        

    def GetDocServer(self, request, context):
        """получение сервера по ид документа
        """
        server_idx = request.docId % len(self.doc_servers)
        server = self.doc_servers[server_idx]

        # check server availability
        channel = grpc.insecure_channel(f"{server['host']}:{server['port']}")
        stub = document_pb2_grpc.DocumentServiceStub(channel)
        try:
            stub.Ping(PingRequest())
        except grpc.RpcError as e:
            self.doc_servers.pop(server_idx)
        
        # if no servers available
        if not self.doc_servers:
            return DocServer(host='', port=0)

        return DocServer(host=server['host'], port=server['port'])

    
    def AddDocServer(self, request, context):
        """добавление нового сервера документов
        """
        if request.secretKey != CFG['secret_key']:
            return AddDocServerResponse(success=False)
        self.doc_servers.append({
            'host': request.docServer.host,
            'port': request.docServer.port,
        })
        return AddDocServerResponse(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dispatcher_pb2_grpc.add_DispatcherServiceServicer_to_server(
        DispatcherService(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    server.wait_for_termination()