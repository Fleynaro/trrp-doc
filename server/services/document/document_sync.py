import threading

class TextChange:
    INSERT = 0
    DELETE = 1

    def __init__(self, type, pos, text):
        self.type = type
        self.pos = pos
        self.text = text
        self.len = len(text)


class DocumentChanges:
    def __init__(self, changes, version):
        self.changes = changes
        self.version = version

    def join(self, other):
        self.changes += other.changes
        self.version = other.version


class DocumentSync:
    def __init__(self, init_text):
        self.init_text = init_text
        self.actual_text = init_text
        self.actual_text_version = 0
        self.changes_history = {0: DocumentChanges([], 0)}
        self.sync = threading.Lock()
        self.history_max_size = 50

    def get_actual_content(self):
        last_version = self.get_last_version()

        if self.actual_text_version < last_version:
            last_changes = self.get_last_changes(self.actual_text_version)
            self.actual_text_version = last_version

            for change in last_changes.changes:
                if change.type == TextChange.INSERT:
                    self.actual_text = self.actual_text[:change.pos] + change.text + self.actual_text[change.pos:]
                elif change.type == TextChange.DELETE:
                    self.actual_text = self.actual_text[:change.pos] + self.actual_text[change.pos+len(change.text):]
                    
        return self.actual_text

    def get_first_version(self):
        return min(self.changes_history.keys())

    def get_last_version(self):
        return max(self.changes_history.keys())

    def version_exists(self, version):
        return version in self.changes_history

    def get_last_changes(self, from_version) -> DocumentChanges:
        last_version = self.get_last_version()
        last_changes = DocumentChanges([], last_version)
        for ver, change in sorted(self.changes_history.items()):
            if ver >= from_version and ver <= last_version:
                last_changes.join(change)

        return last_changes

    def add_changes(self, doc_changes: DocumentChanges):
        new_ver = doc_changes.version + 1
        with self.sync:
            while new_ver <= self.get_last_version():
                # if anybody has made changes after this version, we need to merge them
                stranger_changes = self.changes_history[new_ver]
                for s_ch in stranger_changes.changes:
                    for ch in doc_changes.changes[:]:
                        if s_ch.type == TextChange.INSERT:
                            if s_ch.pos < ch.pos:
                                ch.pos += s_ch.len
                        elif s_ch.type == TextChange.DELETE:
                            if ch.type == TextChange.INSERT:
                                if s_ch.pos + s_ch.len <= ch.pos:
                                    ch.pos -= s_ch.len
                                elif s_ch.pos < ch.pos:
                                    ch.pos = s_ch.pos
                            else:
                                if s_ch.pos + s_ch.len <= ch.pos:
                                    ch.pos -= s_ch.len
                                elif ch.pos + ch.len >= s_ch.pos:
                                    doc_changes.changes.remove(ch)
                new_ver += 1
            self.changes_history[new_ver] = doc_changes
            # remove first version to keep history size
            if len(self.changes_history) > self.history_max_size:
                self.changes_history.pop(self.get_first_version())
