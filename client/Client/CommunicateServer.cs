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
        private string domain;
        //private string documentHost;
        private Channel documentServerChannel;
        private Channel dispatcherChannel;
        private DocumentService.DocumentServiceClient documentClient;
        private DispatcherService.DispatcherServiceClient dispatcherClient;

        public CommunicateServer(string domain = "localhost")
        {
            //var ips = Dns.GetHostAddresses("trrp.mooo.com");
            //var ip = "localhost";
            //ip = ips[0].ToString();
            this.domain = domain;
        }

        public void ConnectToDispatcher()
        {
            try
            {
                dispatcherChannel = new Channel(domain, 30163, ChannelCredentials.Insecure);
                dispatcherClient = new DispatcherService.DispatcherServiceClient(dispatcherChannel);
            }
            catch (RpcException)
            {
                // TODO: Обработать ошибки
                throw new Exception("Не удалось связаться с сервером диспечера");
            }
        }

        public List<DocumentsResponse.Types.DocumentInfo> GetDocuments()
        {
            List<DocumentsResponse.Types.DocumentInfo> documents;
            try
            {
                var request = new DocumentsRequest();
                documents = dispatcherClient.GetDocuments(request, deadline: DateTime.UtcNow.AddSeconds(5)).Documents.ToList();
            }
            catch (RpcException)
            {
                // TODO: Обработать ошибку
                throw new UnavailableDispatcherServerException("Сервер документов недоступен. Поторите попытку позже.");
            }
            return documents;
        }

        public DocServer GetDocServer(long docId)
        {
            DocServer serverResponse;
            try
            {
                var serverRequest = new DocServerRequest() { DocId = docId };

                serverResponse = dispatcherClient.GetDocServer(serverRequest, deadline: DateTime.UtcNow.AddSeconds(5));
            }
            catch (RpcException ex)
            {
                // TODO: Обработать ошибки
                ConnectToDispatcher();
                throw new UnavailableDispatcherServerException("Ошибка получения адреса сервера документа. Проблемы с доступом к диспетчеру.");
            }
            return serverResponse;
        }

        public void ConnectToDocumentServer(string host)
        {
            //documentHost = host;
            try
            {
                documentServerChannel = new Channel(host, ChannelCredentials.Insecure);
                documentClient = new DocumentService.DocumentServiceClient(documentServerChannel);
            }
            catch(RpcException)
            {
                // TODO: Обработать ошибки
                throw new UnavailableDocumentServerException("Рабочий сервер недоступен");
            }
        }

        public DocumentContentResponse GetActualDocumentContent(long docId)
        {
            DocumentContentResponse document;
            try
            {
                var request = new DocumentContentRequest() { DocId = docId };
                document = documentClient.GetActualDocumentContent(request, deadline: DateTime.UtcNow.AddSeconds(5));
            }
            catch (RpcException ex)
            {
                // TODO: Обработать ошибки
                throw new UnavailableDocumentServerException("Ошибка получения актуальной версии документа");
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
                documentChanges = documentClient.GetDocumentChanges(request, deadline: DateTime.UtcNow.AddSeconds(5));
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                if (StatusCode.NotFound == e.StatusCode)
                {
                    throw new NotFoundDocumentException();
                }
                else if (StatusCode.Unavailable == e.StatusCode)
                {
                    //ConnectToDocumentServer(documentHost);
                    throw new UnavailableDocumentServerException("Сервер документа недоступен. Проверьте соединение с сетью.");
                }
                else throw new UnavailableDocumentServerException("Ошибка при получении изменений документа.");
            }
            return documentChanges;
        }

        public void SendDocumentChanges(DocumentChanges documentChanges)
        {
            try
            {
                documentClient.SendDocumentChanges(documentChanges, deadline: DateTime.UtcNow.AddSeconds(5));
            }
            catch (RpcException e)
            {
                // TODO: Обработать ошибки
                if (StatusCode.Unavailable == e.StatusCode)
                {
                    //ConnectToDocumentServer(documentHost);
                    throw new UnavailableDocumentServerException("Сервер документа недоступен. Проверьте соединение с сетью.");
                }
                else
                    throw new UnavailableDocumentServerException("Ошибка отправки изменений. Проверьте соединение с сетью.");
            }
        }
    }
}
