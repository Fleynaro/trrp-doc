using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client
{
    class CommunicateServerException : Exception
    {
        public CommunicateServerException() : base() { }
        public CommunicateServerException(string message) : base(message) { }
    }

    class NotFoundDocumentException : Exception
    {
        public NotFoundDocumentException() : base() { }
        public NotFoundDocumentException(string message) : base(message) { }
    }

    class SendDocumentChangesException : Exception
    {
        public SendDocumentChangesException() : base() { }
        public SendDocumentChangesException(string message) : base(message) { }
    }

    class GetActualDocumentContentException : Exception
    {
        public GetActualDocumentContentException() : base() { }
        public GetActualDocumentContentException(string message) : base(message) { }
    }

    class ConnectToDocumentServerException : Exception
    {
        public ConnectToDocumentServerException() : base() { }
        public ConnectToDocumentServerException(string message) : base(message) { }
    }

    class GetDocServerException : Exception
    {
        public GetDocServerException() : base() { }
        public GetDocServerException(string message) : base(message) { }
    }

    class GetDocumentsException : Exception
    {
        public GetDocumentsException() : base() { }
        public GetDocumentsException(string message) : base(message) { }
    }

    class UnavailableDocumentServerException : Exception
    {
        public UnavailableDocumentServerException() : base() { }
        public UnavailableDocumentServerException(string message) : base(message) { }
    }

    class UnavailableDispatcherServerException : Exception
    {
        public UnavailableDispatcherServerException() : base() { }
        public UnavailableDispatcherServerException(string message) : base(message) { }
    }
}
