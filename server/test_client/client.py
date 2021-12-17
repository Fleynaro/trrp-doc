import grpc

from dispatcher_pb2 import DocServerRequest
import dispatcher_pb2_grpc


def client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = dispatcher_pb2_grpc.DispatcherServiceStub(channel)
    doc_server = stub.GetDocServer(DocServerRequest(docId=1))
    pass