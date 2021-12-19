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
        server_addr = ''

        # try connect to server
        while server_addr == '':
            # if no servers available
            if not self.doc_servers:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('No servers available!')
                return DocServer()

            # select random server
            server_idx = request.docId % len(self.doc_servers)
            server_addr = self.doc_servers[server_idx]

            # check server availability
            channel = grpc.insecure_channel(server_addr)
            stub = document_pb2_grpc.DocumentServiceStub(channel)
            try:
                stub.Ping(PingRequest(docId=request.docId, secretKey=CFG['secret_key']))
            except grpc.RpcError as e:
                self.doc_servers.remove(server_addr)
                server_addr = ''

        return DocServer(address=server_addr)

    
    def AddDocServer(self, request, context):
        """добавление нового сервера документов
        """
        if request.secretKey != CFG['secret_key']:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Permission denied!')
            return AddDocServerResponse()
        self.doc_servers.append(request.docServer.address)
        return AddDocServerResponse()