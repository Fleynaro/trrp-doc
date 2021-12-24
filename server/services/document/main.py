import sys
sys.path.append("./grpc")
sys.path.append("./shared")

from concurrent import futures
import grpc

import document_pb2_grpc

from service import DocumentService

from config import CFG


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    document_pb2_grpc.add_DocumentServiceServicer_to_server(
        DocumentService(), server)
    
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("document server started at {}".format('0.0.0.0:50051'))
    server.wait_for_termination()


if __name__ == '__main__':
    serve()