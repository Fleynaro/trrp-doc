from os import listdir
import grpc

from document_content_pb2 import DocumentContentResponse
from storage_pb2 import DocumentInfoResponse
import storage_pb2_grpc

from config import CFG
from utils import title_to_id


class StorageService(
    storage_pb2_grpc.StorageServiceServicer):
    """сервис по работе со множеством документов
    """
    def __init__(self):
        super().__init__()
        self.load_all_documents()

    def GetDocuments(self, request, context):
        """получение списка документов
        """
        for id, title in self.documents.items():
            yield DocumentInfoResponse(
                id=id,
                title=title,
            )
        
    def GetDocumentContent(self, request, context):
        """получение содержимого документа
        """
        docId = request.docId

        if docId not in self.documents:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Document not found!')
            return DocumentContentResponse()

        doc_dir = CFG['storage']['dir']
        text = ''
        with open(f'{doc_dir}/{self.documents[docId]}', 'r') as f:
            text = f.read()
        return DocumentContentResponse(text=text)

    def load_all_documents(self):
        self.documents = {}
        doc_dir = CFG['storage']['dir']
        for title in listdir(doc_dir):
            self.documents[title_to_id(title)] = title