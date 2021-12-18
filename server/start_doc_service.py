import sys
sys.path.append("./grpc")
sys.path.append("./shared")
sys.path.append("./services/document")

from main import serve

if __name__ == '__main__':
    serve()