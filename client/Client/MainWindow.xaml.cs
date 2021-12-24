using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Doc;
using Grpc.Core;

namespace Client
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private long docId;
        private CommunicateServer server;
        private WordProcessing wordProcessing;
        private DocumentContentResponse documentBackup;
        private List<DocumentsResponse.Types.DocumentInfo> documents;
        private Timer timer;
        private string success = "Успешное подключение к серверам";

        public MainWindow()
        {
            InitializeComponent();
            wordProcessing = new WordProcessing();
            timer = new Timer(SyncDoc);
            try
            {
                server = new CommunicateServer("trrp-disp.mooo.com");
                server.ConnectToDispatcher();
                documents = server.GetDocuments();
                foreach (var doc in documents)
                {
                    documentsList.Items.Add(doc.Title);
                }
            }
            catch(Exception ex)
            {
                logTextBlock.Text = ex.Message;
                //MessageBox.Show(this, ex.Message, "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void GetActualDocument()
        {
            try
            {
                var docServer = server.GetDocServer(docId);
                server.ConnectToDocumentServer(docServer.Address);
                var actualDoc = server.GetActualDocumentContent(docId);
                documentBackup = new DocumentContentResponse()
                {
                    Text = actualDoc.Text,
                    Version = actualDoc.Version
                };
                ChangeTextInRichTextBox(actualDoc.Text);
                logTextBlock.Text = success;
            }
            catch (UnavailableDispatcherServerException ex)
            {
                throw ex;
            }
            catch (UnavailableDocumentServerException ex)
            {
                throw ex;
            }
        }

        private void LoadDocumentFromServer(object sender, RoutedEventArgs e)
        {
            try
            {
                var doc = documents.Where(z => z.Title == documentsList.SelectedItem.ToString()).First();
                docId = doc.DocId;
                server.ConnectToDispatcher();
                GetActualDocument();
                timer.Start();
            }
            catch (UnavailableDocumentServerException)
            {
                logTextBlock.Text = "Попытка переподключения к рабочему серверу провалилась";
                //throw new UnavailableDocumentServerException("Попытка переподключения к рабочему серверу провалилась");
            }
            catch (UnavailableDispatcherServerException)
            {
                logTextBlock.Text = "Попытка переподключения к диспетчеру провалилась";
            }
        }

        private void SyncDoc(object sender, EventArgs e)
        {
            try
            {
                SendDiffToServer();
                ReceiveDiffFromServer();
                logTextBlock.Text = success;
            }
            catch (Exception ex)
            {
                logTextBlock.Text = ex.Message;
                //MessageBox.Show(this, ex.Message, "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void SendDiffToServer()
        {
            var newText = GetTextFromRichTextBox();
            var oldText = documentBackup.Text;
            var dataForSend = new DocumentChanges()
            {
                DocId = docId,
                Version = documentBackup.Version
            };
            wordProcessing.Compare(oldText, newText, dataForSend);
            try
            {
                if (dataForSend.Changes.Count != 0)
                    server.SendDocumentChanges(dataForSend);
            }
            catch(UnavailableDocumentServerException)
            {
                GetActualDocument();
            }
        }

        private void ReceiveDiffFromServer()
        {
            DocumentChanges docChanges;
            try
            {
                docChanges = server.GetDocumentChanges(docId, documentBackup.Version);
            }
            catch(NotFoundDocumentException)
            {
                GetActualDocument();
                docChanges = server.GetDocumentChanges(docId, documentBackup.Version);
            }
            catch (UnavailableDocumentServerException)
            {
                GetActualDocument();
                docChanges = server.GetDocumentChanges(docId, documentBackup.Version);
            }
            if (docChanges.Changes.Count != 0)
            {
                var text = documentBackup.Text;
                var newText = wordProcessing.ApplyTextChanges(text, docChanges);
                docId = docChanges.DocId;
                documentBackup.Version = docChanges.Version;
                documentBackup.Text = newText;
                ChangeTextInRichTextBox(newText);
            }
        }

        private void ChangeTextInRichTextBox(string text)
        {
            var docChanges = new DocumentChanges();
            //wordProcessing.Compare(GetTextFromRichTextBox(), text, docChanges);
            wordProcessing.Compare(documentBackup.Text, text, docChanges);

            int prevCursorPos = GetCaretPos();
            int offset = prevCursorPos;
            for (int i = 0; i < docChanges.Changes.Count; i++)
            {
                var change = docChanges.Changes[i];
                if (change.Pos >= prevCursorPos)
                    continue;
                if (change.Type == DocumentChanges.Types.ChangeType.Insert)
                {
                    offset += change.Text.Length;
                }
                else if (change.Type == DocumentChanges.Types.ChangeType.Delete)
                {
                    offset -= change.Text.Length;
                }
            }

            docBox.Document.Blocks.Clear();
            docBox.Document.Blocks.Add(new Paragraph(new Run(text)));
            docBox.CaretPosition = docBox.Document.ContentStart;
            int nl_count = 0;
            for (int i = 0; i < text.Length; ++i)
            {
                if (i >= offset)
                    break;
                if (text[i] == '\n')
                    nl_count++;
            }

            for (int i = 0; i < Math.Abs(offset) - nl_count && i < text.Length - nl_count; ++i)
                docBox.CaretPosition = docBox.CaretPosition.GetNextInsertionPosition(offset > 0 ? LogicalDirection.Forward : LogicalDirection.Backward);
        }

        private int GetCaretPos()
        {
            TextPointer start = docBox.Document.ContentStart;
            TextPointer caret = docBox.CaretPosition;
            TextRange range = new TextRange(start, caret);
            return range.Text.Length;
        }

        private string GetTextFromRichTextBox()
        {
            var text = new TextRange(docBox.Document.ContentStart, docBox.Document.ContentEnd).Text;
            return text.Substring(0, text.Length - 2);
        }
    }
}
