import sys
sys.path.append("../grpc")

import time
import grpc

from dispatcher_pb2 import DocServerRequest, DocumentsRequest
from document_pb2 import DocumentChangesRequest, DocumentChanges, DocumentContentRequest
import dispatcher_pb2_grpc
import document_pb2_grpc


def apply_changes(text, changes):
    return text # новый измененный текст


def client():
    # диспетчер серверов
    channel = grpc.insecure_channel("127.0.0.1:50051")
    dispatcher_stub = dispatcher_pb2_grpc.DispatcherServiceStub(channel)

    # получаем список доступных документов
    response = dispatcher_stub.GetDocuments(DocumentsRequest())
    # выбираем первый документ
    my_doc = response.documents[0]


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
    my_doc_text += "I am alex!"
    # отправляем изменения, сделанные относительно версии полученного документа через GetActualDocumentContent
    doc_stub.SendDocumentChanges(DocumentChanges(
        docId=my_doc.docId,
        version=response.version,
        changes=[
            DocumentChanges.Change(
                type=DocumentChanges.CHANGE_TYPE_INSERT,
                pos=len(my_doc_prev_text),
                text="I am alex!")
            ]
    ))

    # параллельное редактирование несколькими людьми
    if True:
        my_doc_text += " I am fleynaro!"
        doc_stub.SendDocumentChanges(DocumentChanges(
            docId=my_doc.docId,
            version=response.version,
            changes=[
                DocumentChanges.Change(
                    type=DocumentChanges.CHANGE_TYPE_INSERT,
                    pos=len(my_doc_prev_text),
                    text="I am fleynaro!")
                ]
        ))

        text = doc_stub.GetActualDocumentContent(DocumentContentRequest(docId=my_doc.docId)).text
        print(text)

    # получаем последние изменения в документе
    doc_last_changes = doc_stub.GetDocumentChanges(DocumentChangesRequest(docId=my_doc.docId, version=response.version))
    # применяем полученные изменения к содержимому my_doc_prev_text (а не my_doc_text)
    my_doc_text = apply_changes(my_doc_prev_text, doc_last_changes)
    print(my_doc_text)


if __name__ == '__main__':
    client()