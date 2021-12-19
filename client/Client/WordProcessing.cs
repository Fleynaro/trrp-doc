using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DiffMatchPatch;
using Doc;

namespace Client
{
    class WordProcessing
    {
        private diff_match_patch dmp;

        public WordProcessing()
        {
            dmp = new diff_match_patch();
        }

        public void Compare(string oldText, string newText, DocumentChanges changes)
        {
            var diff = dmp.diff_main(oldText, newText);
            dmp.diff_cleanupSemantic(diff);
            GenerateDifferences(diff, changes);
        }

        private void GenerateDifferences(List<Diff> diffs, DocumentChanges changes)
        {
            long position = 0;

            foreach (var diff in diffs)
            {
                switch(diff.operation)
                {
                    case Operation.INSERT:
                        changes.Changes.Add(new DocumentChanges.Types.Change()
                        {
                            Type = DocumentChanges.Types.ChangeType.Insert,
                            Pos = position,
                            Text = diff.text
                        });
                        position += diff.text.Length;
                        break;
                    case Operation.DELETE:
                        changes.Changes.Add(new DocumentChanges.Types.Change()
                        {
                            Type = DocumentChanges.Types.ChangeType.Delete,
                            Pos = position,
                            Text = diff.text
                        });
                        break;
                    case Operation.EQUAL:
                        position += diff.text.Length;
                        break;
                }
            }
        }

        public string ApplyTextChanges(string text, DocumentChanges changes)
        {
            var sb = new StringBuilder(text);

            foreach (var change in changes.Changes)
            {
                switch (change.Type)
                {
                    case DocumentChanges.Types.ChangeType.Insert:
                        sb.Insert((int)change.Pos, change.Text);
                        break;
                    case DocumentChanges.Types.ChangeType.Delete:
                        sb.Remove((int)change.Pos, change.Text.Length);
                        break;
                }
            }

            return sb.ToString();
        }
    }
}
