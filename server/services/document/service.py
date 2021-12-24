import grpc

import document_sync as ds

from document_pb2 import AddDocumentResponse, DocumentChanges, DocumentChangesResponse, DocumentContentResponse
import document_pb2_grpc

from config import CFG

from google.cloud import storage

class DocumentService(document_pb2_grpc.DocumentServiceServicer):
    """сервис по работе с одним документом
    """
    def __init__(self):
        super().__init__()
        storage_client = storage.Client()
        self.doc_bucket = storage_client.get_bucket(CFG['storage_bucket'])
        self.active_documents = {}

    def AddDocument(self, request, context):
        """проверка доступности сервера
        """
        if request.secretKey != CFG['secret_key']:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Permission denied!')
            return AddDocumentResponse()
        docId = request.docId
        if docId not in self.active_documents:
            # load the document and make it active
            doc_title = f"doc{docId}.txt"
            doc_blob = self.doc_bucket.blob(doc_title)
            doc_blob.download_to_filename(doc_title)
            with open(doc_title, "r") as f:
                self.active_documents[docId] = ds.DocumentSync(f.read())
        return AddDocumentResponse()

    def GetActualDocumentContent(self, request, context):
        """получение контента документа актуальной версии
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentContentResponse()
        text, version = doc_sync.get_actual_content()
        return DocumentContentResponse(text=text, version=version)

    def GetDocumentChanges(self, request, context):
        """получить изменения
        """
        doc_sync = self.get_doc_sync(request.docId, context)
        if not doc_sync:
            return DocumentChanges()
        if not self.version_exists(doc_sync, request.version, context):
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
        if not self.version_exists(doc_sync, request.version, context):
            return DocumentChangesResponse()

        doc_changes = ds.DocumentChanges(
            changes=[ds.TextChange(ch.type, ch.pos, ch.text) for ch in request.changes],
            version=request.version
        )

        doc_sync.add_changes(doc_changes)
        # save
        #text, version = doc_sync.get_actual_content()
        #doc_title = f"doc{request.docId}.txt"
        #doc_blob = self.doc_bucket.blob(doc_title)
        #doc_blob.upload_from_string(text)

        return DocumentChangesResponse()

    def get_doc_sync(self, doc_id, context) -> ds.DocumentSync:
        """проверка наличия документа
        """
        if doc_id not in self.active_documents:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Document not found!')
            return None
        return self.active_documents[doc_id]

    def version_exists(self, doc_sync: ds.DocumentSync, version: int, context):
        """проверка наличия версии
        """
        if doc_sync.version_exists(version):
            return True
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Version {} not found!".format(version))
        return False