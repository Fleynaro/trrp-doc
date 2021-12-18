
class DocumentChanges:
    def __init__(self):
        self.inserts = []
        self.deletes = []

class DocumentSync:
    def __init__(self, init_text):
        self.init_text = init_text
        self.changes_history = []

    def get_actual_content(self):
        return self.init_text