import sys
sys.path.append("./grpc")
sys.path.append("./shared")
sys.path.append("./services/storage")

from main import serve

if __name__ == '__main__':
    serve()