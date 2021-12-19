from concurrent import futures
import grpc

import storage_pb2_grpc

from service import StorageService

from config import CFG

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storage_pb2_grpc.add_StorageServiceServicer_to_server(
        StorageService(), server)
    server.add_insecure_port(CFG['storage_address'])
    server.start()
    server.wait_for_termination()