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
        private List<DocumentInfoResponse> documents;
        private DispatcherTimer timer;

        public MainWindow()
        {
            InitializeComponent();
            wordProcessing = new WordProcessing();
            CreateTimer();
            server = new CommunicateServer("localhost", 50051);
            server.GetDocuments(documents).Wait();
            foreach (var doc in documents)
            {
                documentsList.Items.Add(doc.Title);
            }
        }

        private void CreateTimer()
        {
            timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromMilliseconds(500);
            timer.Tick += SyncDoc;
        }

        private void LoadDocumentFromServer(object sender, RoutedEventArgs e)
        {
            if (timer.IsEnabled)
                timer.Stop();

            var doc = documents.Where(z => z.Title == documentsList.SelectedItem.ToString()).First();
            docId = doc.DocId;
            var docServer = server.GetDocServer(doc.DocId);
            server.ConnectToDocumentServer(docServer.Address);
            var actualDoc = server.GetActualDocumentContent(doc.DocId);
            documentBackup = new DocumentContentResponse()
            {
                Text = actualDoc.Text,
                Version = actualDoc.Version
            };
            ChangeTextInRichTextBox(actualDoc.Text);

            timer.Start();
        }

        private void SyncDoc(object sender, EventArgs e)
        {
            SendDiffToServer();
            ReceiveDiffFromServer();
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
            server.SendDocumentChanges(dataForSend);
        }

        private void ReceiveDiffFromServer()
        {
            var docChanges = server.GetDocumentChanges(docId, documentBackup.Version);
            var text = documentBackup.Text;
            var newText = wordProcessing.ApplyTextChanges(text, docChanges);
            ChangeTextInRichTextBox(newText);
        }

        private void ChangeTextInRichTextBox(string text)
        {
            docBox.Document.Blocks.Clear();
            docBox.Document.Blocks.Add(new Paragraph(new Run(text)));
        }

        private string GetTextFromRichTextBox()
        {
            return new TextRange(docBox.Document.ContentStart, docBox.Document.ContentEnd).Text;
        }
    }
}
