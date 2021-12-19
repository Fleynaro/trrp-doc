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
using System.Windows.Threading;
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
        private DispatcherTimer timer;

        public MainWindow()
        {
            InitializeComponent();
            wordProcessing = new WordProcessing();
            CreateTimer();
            try
            {
                server = new CommunicateServer();
                documents = server.GetDocuments();
                foreach (var doc in documents)
                {
                    documentsList.Items.Add(doc.Title);
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void CreateTimer()
        {
            timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromMilliseconds(1000);
            timer.Tick += SyncDoc;
        }

        private void LoadDocumentFromServer(object sender, RoutedEventArgs e)
        {
            if (timer.IsEnabled)
                timer.Stop();

            try
            {
                var doc = documents.Where(z => z.Title == documentsList.SelectedItem.ToString()).First();
                docId = doc.DocId;
                var docServer = server.GetDocServer(docId);
                server.ConnectToDocumentServer(docServer.Address);
                var actualDoc = server.GetActualDocumentContent(docId);
                documentBackup = new DocumentContentResponse()
                {
                    Text = actualDoc.Text,
                    Version = actualDoc.Version
                };
                ChangeTextInRichTextBox(actualDoc.Text);
                timer.Start();
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void SyncDoc(object sender, EventArgs e)
        {
            try
            {
                SendDiffToServer();
                ReceiveDiffFromServer();
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
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
            if (dataForSend.Changes.Count != 0)
                server.SendDocumentChanges(dataForSend);
        }

        private void ReceiveDiffFromServer()
        {
            DocumentChanges docChanges;
            try
            {
                docChanges = server.GetDocumentChanges(docId, documentBackup.Version);
            }
            catch(GetDocumentChangesException)
            {
                LoadDocumentFromServer(this, new RoutedEventArgs());
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

        //private void TestCursor(object sender, RoutedEventArgs e)
        //{
        //    var caret = docBox.CaretPosition;
        //    docBox.Focus();
        //    docBox.CaretPosition = docBox.CaretPosition.GetNextInsertionPosition(LogicalDirection.Forward);
        //}

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
