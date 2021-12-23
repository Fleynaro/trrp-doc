import sys
sys.path.append("./grpc")
sys.path.append("./shared")

from concurrent import futures
import grpc

import dispatcher_pb2_grpc

from service import DispatcherService

from config import CFG

def serve():
    print("starting dispatcher...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dispatcher_pb2_grpc.add_DispatcherServiceServicer_to_server(
        DispatcherService(), server)
    server.add_insecure_port(CFG['dispatcher_address'])
    server.start()
    print("dispatcher started at {}".format(CFG['dispatcher_address']))
    server.wait_for_termination()


if __name__ == '__main__':
    serve()