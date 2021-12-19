
class TextChange:
    def __init__(self, type, pos, text):
        self.type = type
        self.pos = pos
        self.text = text


class DocumentChanges:
    def __init__(self):
        self.changes = []
        self.version = 0

    def join(self, other):
        self.changes.extend(other.changes)
        self.version = other.version


class DocumentSync:
    def __init__(self, init_text):
        self.init_text = init_text
        self.changes_history = [DocumentChanges()]

    def get_actual_content(self):
        return self.init_text

    def get_last_changes(self, from_version) -> DocumentChanges:
        last_changes = self.changes_history[from_version]
        for change in self.changes_history[from_version+1:]:
            last_changes.join(change)
        return last_changes
