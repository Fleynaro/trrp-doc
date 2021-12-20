using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
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

        public CommunicateServer()
        {
            var ips = Dns.GetHostAddresses("trrp.mooo.com");
            var ip = "localhost";
            ip = ips[0].ToString();
            try
            {
                storageChannel = new Channel(ip, 50052, ChannelCredentials.Insecure);
                storageClient = new StorageService.StorageServiceClient(storageChannel);

                dispatcherChannel = new Channel(ip, 50051, ChannelCredentials.Insecure);
                dispatcherClient = new DispatcherService.DispatcherServiceClient(dispatcherChannel);
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                throw new Exception("Не удалось связаться с серверми диспечера и документов");
            }
        }

        public List<DocumentsResponse.Types.DocumentInfo> GetDocuments()
        {
            List<DocumentsResponse.Types.DocumentInfo> documents;
            try
            {
                var request = new DocumentsRequest();
                documents = storageClient.GetDocuments(request).Documents.ToList();
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибку
                throw new Exception("Сервер документов недоступен. Поторите попытку позже.");
            }
            return documents;
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
                throw new Exception("Ошибка получения адреса сервера документа. Проблемы с доступом к диспетчеру.");
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
                throw new Exception("Сервер документа недоступен");
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
                throw new Exception("Ошибка получения актуальной версии документа");
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
                if (StatusCode.NotFound == e.StatusCode)
                {
                    throw new GetDocumentChangesException();
                }
                else if (StatusCode.Unavailable == e.StatusCode)
                    throw new Exception("Сервер документа недоступен. Проверьте соединение с сетью.");
                else throw new Exception("Ошибка при получении изменений документа.");
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
                throw new Exception("Ошибка отправки изменений. Проверьте соединение с сетью.");
            }
        }
    }
}
