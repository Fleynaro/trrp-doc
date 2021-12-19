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
            var text = documentBackup.Text;
            var newText = wordProcessing.ApplyTextChanges(text, docChanges);
            docId = docChanges.DocId;
            documentBackup.Version = docChanges.Version;
            documentBackup.Text = newText;
            ChangeTextInRichTextBox(newText);
        }

        private void ChangeTextInRichTextBox(string text)
        {
            docBox.Document.Blocks.Clear();
            docBox.Document.Blocks.Add(new Paragraph(new Run(text)));
            docBox.CaretPosition = docBox.CaretPosition.DocumentEnd;
        }

        private string GetTextFromRichTextBox()
        {
            var text = new TextRange(docBox.Document.ContentStart, docBox.Document.ContentEnd).Text;
            return text.Substring(0, text.Length - 2);
        }
    }
}
