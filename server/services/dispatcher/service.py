import grpc

from dispatcher_pb2 import DocServer, AddDocServerResponse
from document_pb2 import PingRequest
import dispatcher_pb2_grpc
import document_pb2_grpc

from config import CFG


class DispatcherService(
    dispatcher_pb2_grpc.DispatcherServiceServicer):
    """сервис по работе со множеством серверов
    """
    def __init__(self):
        super().__init__()
        self.doc_servers = []
        

    def GetDocServer(self, request, context):
        """получение сервера по ид документа
        """
        server_idx = request.docId % len(self.doc_servers)
        server = self.doc_servers[server_idx]

        # check server availability
        channel = grpc.insecure_channel(f"{server['host']}:{server['port']}")
        stub = document_pb2_grpc.DocumentServiceStub(channel)
        try:
            stub.Ping(PingRequest(docId=request.docId))
        except grpc.RpcError as e:
            # todo: исполнение кода параллельное или асинхронное?
            self.doc_servers.pop(server_idx)
        
        # if no servers available
        if not self.doc_servers:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No servers available!')
            return DocServer()

        return DocServer(host=server['host'], port=server['port'])

    
    def AddDocServer(self, request, context):
        """добавление нового сервера документов
        """
        if request.secretKey != CFG['secret_key']:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Permission denied!')
            return AddDocServerResponse()
        self.doc_servers.append({
            'host': request.docServer.host,
            'port': request.docServer.port,
        })
        return AddDocServerResponse()