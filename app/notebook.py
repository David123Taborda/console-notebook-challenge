# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code:str, title:str, text:str, importance:str, creation_date:datetime):
        self.code = code
        self.title= title
        self.text= text
        self.importance= importance
        self.datatime= datetime.now()
        self.tags= []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        new_note = Note(code, title, text, importance)
        self.notes.append(new_note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes if note.importance in (Note.HIGH, Note.MEDIUM)]

    def notes_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_counts = Counter(tag for note in self.notes for tag in note.tags)
        if not tag_counts:
            return ""
        return min(tag_counts, key=lambda tag: (-tag_counts[tag], tag))


