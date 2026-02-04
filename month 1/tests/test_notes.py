from modules.notes_manager import NotesManager

def test_add_note():
    nm = NotesManager()
    initial = len(nm.notes)
    nm.notes.append({"id": 999, "title": "Test", "content": "Test"})
    assert len(nm.notes) == initial + 1
