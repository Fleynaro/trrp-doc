import grpc

from dispatcher_pb2 import DocServer, DocumentsResponse
from document_pb2 import AddDocumentRequest
import dispatcher_pb2_grpc
import document_pb2_grpc

from config import CFG

import kubernetes as k8s

class DispatcherService(
    dispatcher_pb2_grpc.DispatcherServiceServicer):
    """сервис по работе со множеством серверов
    """
    def __init__(self):
        super().__init__()
        self.doc_servers = [
            'trrp.mooo.com:30001',
            'trrp.mooo.com:30002',
        ]
        

    def GetDocServer(self, request, context):
        """получение сервера по ид документа
        """
        # select random server
        server_idx = request.docId % len(self.doc_servers)
        server_addr = self.doc_servers[server_idx]

        # check server availability
        channel = grpc.insecure_channel(server_addr)
        stub = document_pb2_grpc.DocumentServiceStub(channel)
        try:
            stub.AddDocument(AddDocumentRequest(docId=request.docId, secretKey=CFG['secret_key']))
        except grpc.RpcError as e:
            self.doc_servers.remove(server_addr)
            server_addr = ''
        return DocServer(address=server_addr)


    def GetDocuments(self, request, context):
        """получение списка документов
        """
        response = DocumentsResponse()
        response.documents.append(
            DocumentsResponse.DocumentInfo(docId=100, title=f'doc1.txt'))
        response.documents.append(
            DocumentsResponse.DocumentInfo(docId=101, title=f'doc2.txt'))
        return response


def test_kuber():
    response = DocumentsResponse()
    k8s.config.load_incluster_config()
    v1 = k8s.client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        response.documents.append(
            DocumentsResponse.DocumentInfo(docId=100, title=f'{i.status.pod_ip}/{i.metadata.name}'))