import grpc

from document_sync import DocumentSync

from document_content_pb2 import DocumentContentResponse
from document_pb2 import PingResponse, DocumentChanges, DocumentChangesResponse
import document_pb2_grpc
import storage_pb2_grpc

from config import CFG


class DocumentService(document_pb2_grpc.DocumentServiceServicer):
    """сервис по работе с одним документом
    """
    def __init__(self):
        super().__init__()
        channel = grpc.insecure_channel(CFG['storage_address'])
        self.storage_stub = storage_pb2_grpc.StorageServiceStub(channel)
        self.active_documents = {}

    def Ping(self, request, context):
        """проверка доступности сервера
        """
        if request.secretKey != CFG['secret_key']:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Permission denied!')
            return PingResponse()
        docId = request.docId
        if docId not in self.active_documents:
            # load the document and make it active
            response = self.storage_stub.GetDocumentContent(docId=docId)
            self.active_documents[docId] = DocumentSync(response['text'])
        return PingResponse()

    def GetActualDocumentContent(self, request, context):
        """получение контента документа актуальной версии
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentContentResponse()
        return DocumentContentResponse(text=doc_sync.get_actual_content())

    def GetDocumentChanges(self, request, context):
        """получить изменения
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentContentResponse()
        # doc_sync.get_changes()
        return DocumentChanges()

    def SendDocumentChanges(self, request, context):
        """отправить изменения
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentContentResponse()
        return DocumentChangesResponse()

    def get_doc_sync(self, doc_id, context) -> DocumentSync:
        """проверка наличия документа
        """
        if doc_id not in self.active_documents:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Document not found!')
            return None
        return self.active_documents[doc_id]
        