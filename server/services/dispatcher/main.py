from concurrent import futures
import grpc

import dispatcher_pb2_grpc

from service import DispatcherService

from config import CFG

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dispatcher_pb2_grpc.add_DispatcherServiceServicer_to_server(
        DispatcherService(), server)
    server.add_insecure_port(CFG['dispatcher_address'])
    server.start()
    server.wait_for_termination()