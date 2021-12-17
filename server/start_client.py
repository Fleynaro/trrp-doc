import sys
sys.path.append("./grpc")
sys.path.append("./test_client")

from client import client

if __name__ == '__main__':
    client()