from concurrent import futures
import grpc

from dispatcher_pb2 import DocServer
import dispatcher_pb2_grpc
import document_pb2_grpc

from service import DocumentService

from config import CFG


def notify_dispatcher(port):
    """уведомляем диспетчера о новом сервере
    """
    channel = grpc.insecure_channel(CFG['dispatcher_address'])
    stub = dispatcher_pb2_grpc.DispatcherServiceStub(channel)
    host, port = CFG['document_address'].split(':')
    doc_server = DocServer(host, int(port))
    response = stub.AddDocServer(doc_server)
    if not response.success:
        raise Exception('The dispatcher rejected connection request.')
    print('Server has connected to the dispatcher')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    document_pb2_grpc.add_DocumentServiceServicer_to_server(
        DocumentService(), server)
    
    # select port automatically
    port = server.add_insecure_port('0.0.0.0')
    notify_dispatcher(port)

    server.start()
    server.wait_for_termination()