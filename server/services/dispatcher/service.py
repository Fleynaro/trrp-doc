import grpc

from dispatcher_pb2 import DocServer, DocumentsResponse
from document_pb2 import AddDocumentRequest
import dispatcher_pb2_grpc
import document_pb2_grpc

from config import CFG

from google.cloud import storage
import kubernetes as k8s

from utils import title_to_id

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
        storage_client = storage.Client()
        self.doc_bucket = storage_client.get_bucket(CFG['storage_bucket'])
        

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
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details('Document server unavailable!')
            return DocServer()
        return DocServer(address=server_addr)


    def GetDocuments(self, request, context):
        """получение списка документов
        """
        response = DocumentsResponse()
        #for title in self.doc_bucket.list_blobs():
        #    response.documents.append(
        #        DocumentsResponse.DocumentInfo(docId=title_to_id(title), title=title))
        response.documents.append(
            DocumentsResponse.DocumentInfo(docId=1, title=f'doc1.txt'))
        response.documents.append(
            DocumentsResponse.DocumentInfo(docId=2, title=f'doc2.txt'))
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