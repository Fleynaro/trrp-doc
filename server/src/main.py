from concurrent import futures
import grpc

from dispatcher_pb2 import DocServerResponse
import dispatcher_pb2_grpc

from other import t


class DispatcherService(
    dispatcher_pb2_grpc.DispatcherServiceServicer):
    """сервис по работе со множеством документов
    """

    def GetDocuments(self, request, context):
        """получение списка документов
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDocServer(self, request, context):
        """получение сервера по ид документа
        """
        doc_id = request.docId
        return DocServerResponse(host='localhost', port=50051)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dispatcher_pb2_grpc.add_DispatcherServiceServicer_to_server(
        DispatcherService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()