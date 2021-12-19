import grpc

from dispatcher_pb2 import DocServerRequest
from storage_pb2 import DocumentsRequest
from document_content_pb2 import DocumentContentRequest
from document_pb2 import DocumentChangesRequest, DocumentChanges
import dispatcher_pb2_grpc
import storage_pb2_grpc
import document_pb2_grpc


def apply_changes(text, changes):
    return text # новый измененный текст


def client():
    # диспетчер серверов
    channel = grpc.insecure_channel("localhost:50051")
    dispatcher_stub = dispatcher_pb2_grpc.DispatcherServiceStub(channel)
    # хранилище документов
    channel = grpc.insecure_channel("localhost:50052")
    storage_stub = storage_pb2_grpc.StorageServiceStub(channel)


    # получаем список доступных документов
    documents = [d for d in storage_stub.GetDocuments(DocumentsRequest())]
    # выбираем первый документ
    my_doc = documents[0]


    # получаем сервер для работы с данным документом
    doc_server = dispatcher_stub.GetDocServer(DocServerRequest(docId=my_doc.docId))
    channel = grpc.insecure_channel(doc_server.address)
    doc_stub = document_pb2_grpc.DocumentServiceStub(channel)

    # запрашиваем содержимое данного документа
    response = doc_stub.GetActualDocumentContent(DocumentContentRequest(docId=my_doc.docId))
    my_doc_text = response.text
    print(my_doc_text)

    # делаем изменения в содержимом через "редактор" (вставка в конец)
    my_doc_prev_text = my_doc_text # !!!сохраняем содержимое документа до изменений!!!
    my_doc_text += " hello!"
    # отправляем изменения, сделанные относительно версии полученного документа через GetActualDocumentContent
    doc_stub.SendDocumentChanges(DocumentChanges(
        docId=my_doc.docId,
        version=response.version,
        changes=[
            DocumentChanges.Change(
                type=DocumentChanges.CHANGE_TYPE_INSERT,
                pos=len(my_doc_text),
                text="hello!")
            ]
    ))

    # получаем последние изменения в документе
    doc_last_changes = doc_stub.GetDocumentChanges(DocumentChangesRequest(docId=my_doc.docId, version=response.version))
    # применяем полученные изменения к содержимому my_doc_prev_text (а не my_doc_text)
    my_doc_text = apply_changes(my_doc_prev_text, doc_last_changes)
    print(my_doc_text)