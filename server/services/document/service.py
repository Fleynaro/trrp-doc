import grpc

import document_sync as doc_sync

from document_content_pb2 import DocumentContentRequest, DocumentContentResponse
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
            response = self.storage_stub.GetDocumentContent(DocumentContentRequest(docId=docId))
            self.active_documents[docId] = doc_sync.DocumentSync(response.text)
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
            return DocumentChanges()

        doc_changes = doc_sync.get_last_changes(request.version)

        return DocumentChanges(
            docId = request.docId,
            version=doc_changes.version,
            changes=[
                DocumentChanges.Change(
                    type=ch.type,
                    pos=ch.pos,
                    text=ch.text) for ch in doc_changes.changes]
        )

    def SendDocumentChanges(self, request, context):
        """отправить изменения
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentChangesResponse()

        # ...

        return DocumentChangesResponse()

    def get_doc_sync(self, doc_id, context) -> doc_sync.DocumentSync:
        """проверка наличия документа
        """
        if doc_id not in self.active_documents:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Document not found!')
            return None
        return self.active_documents[doc_id]
        