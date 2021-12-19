using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Doc;
using Grpc.Core;

namespace Client
{
    class CommunicateServer
    {
        private Channel documentServerChannel;
        private Channel storageChannel;
        private Channel dispatcherChannel;
        private DocumentService.DocumentServiceClient documentClient;
        private DispatcherService.DispatcherServiceClient dispatcherClient;
        private StorageService.StorageServiceClient storageClient;

        public CommunicateServer(string ip, int port)
        {
            try
            {
                storageChannel = new Channel(ip, port, ChannelCredentials.Insecure);
                storageClient = new StorageService.StorageServiceClient(storageChannel);

                dispatcherChannel = new Channel(ip, port, ChannelCredentials.Insecure);
                dispatcherClient = new DispatcherService.DispatcherServiceClient(dispatcherChannel);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
        }

        public async Task GetDocuments(List<DocumentInfoResponse> documents)
        {
            try
            {
                var documentRequest = new DocumentsRequest();
                using (var call = storageClient.GetDocuments(documentRequest))
                {
                    var responseStream = call.ResponseStream;
                    while(await responseStream.MoveNext())
                    {
                        documents.Add(responseStream.Current);
                    }
                }
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибку
                throw;
            }
        }

        public DocServer GetDocServer(long docId)
        {
            DocServer serverResponse;
            try
            {
                var serverRequest = new DocServerRequest() { DocId = docId };

                serverResponse = dispatcherClient.GetDocServer(serverRequest);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
            return serverResponse;
        }

        public void ConnectToDocumentServer(string host)
        {
            try
            {
                documentServerChannel = new Channel(host, ChannelCredentials.Insecure);
                documentClient = new DocumentService.DocumentServiceClient(documentServerChannel);
            }
            catch(RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
        }

        public DocumentContentResponse GetActualDocumentContent(long docId)
        {
            DocumentContentResponse document;
            try
            {
                var request = new DocumentContentRequest() { DocId = docId };
                document = documentClient.GetActualDocumentContent(request);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
            return document;
        }

        public DocumentChanges GetDocumentChanges(long docId, int version)
        {
            DocumentChanges documentChanges;
            try
            {
                var request = new DocumentChangesRequest() {
                    DocId = docId,
                    Version = version
                };
                documentChanges = documentClient.GetDocumentChanges(request);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
            return documentChanges;
        }

        public void SendDocumentChanges(DocumentChanges documentChanges)
        {
            try
            {
                documentClient.SendDocumentChanges(documentChanges);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw;
            }
        }
    }
}
