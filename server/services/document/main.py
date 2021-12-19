from concurrent import futures
import grpc

from dispatcher_pb2 import DocServer, AddDocServerRequest
import dispatcher_pb2_grpc
import document_pb2_grpc

from service import DocumentService

from config import CFG


def notify_dispatcher(port):
    """уведомляем диспетчера о новом сервере
    """
    channel = grpc.insecure_channel(CFG['dispatcher_address'])
    stub = dispatcher_pb2_grpc.DispatcherServiceStub(channel)

    host, _ = CFG['document_address'].split(':')
    stub.AddDocServer(AddDocServerRequest(
        docServer = DocServer(address=f"{host}:{port}"),
        secretKey = CFG['secret_key']))

    print('Server has connected to the dispatcher')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    document_pb2_grpc.add_DocumentServiceServicer_to_server(
        DocumentService(), server)
    
    # select port automatically
    port = server.add_insecure_port(CFG['document_address'])
    notify_dispatcher(port)

    server.start()
    server.wait_for_termination()