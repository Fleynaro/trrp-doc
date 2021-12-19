
class TextChange:
    INSERT = 0
    DELETE = 1

    def __init__(self, type, pos, text):
        self.type = type
        self.pos = pos
        self.text = text


class DocumentChanges:
    def __init__(self, changes=[], version=0):
        self.changes = changes
        self.version = version

    def join(self, other):
        self.changes.extend(other.changes)
        self.version = other.version


class DocumentSync:
    def __init__(self, init_text):
        self.init_text = init_text
        self.actual_text = init_text
        self.actual_text_version = 0
        self.changes_history = [DocumentChanges()]

    def get_actual_content(self):
        if self.actual_text_version < self.get_last_version():
            last_changes = self.get_last_changes(self.actual_text_version)
            self.actual_text_version = self.get_last_version()
            for change in last_changes.changes:
                if change.type == TextChange.INSERT:
                    self.actual_text = self.actual_text[:change.pos] + change.text + self.actual_text[change.pos:]
                elif change.type == TextChange.DELETE:
                    self.actual_text = self.actual_text[:change.pos] + self.actual_text[change.pos+len(change.text):]
        return self.actual_text

    def get_last_version(self):
        return len(self.changes_history) - 1

    def get_last_changes(self, from_version) -> DocumentChanges:
        last_changes = self.changes_history[from_version]
        for change in self.changes_history[from_version+1:]:
            last_changes.join(change)
        return last_changes

    def add_changes(self, changes: DocumentChanges):
        cur_ver = changes.version
        if cur_ver == self.get_last_version():
            self.changes_history.append(changes)
            return
        self.changes_history[cur_ver + 1]
