from dataclasses import dataclass, field, asdict
from pathlib import Path
import json
from typing import List, Optional

@dataclass
class Note:
    id: int
    title: str
    content: str
    tags: List[str] = field(default_factory=list)

class StudyLibrary:
    """Simple library for storing study notes."""

    def __init__(self, path: str = "notes.json"):
        self.path = Path(path)
        self.notes: List[Note] = []
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.notes = [Note(**item) for item in data]
        else:
            self.notes = []

    def _save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump([asdict(n) for n in self.notes], f, ensure_ascii=False, indent=2)

    def add(self, title: str, content: str, tags: Optional[List[str]] = None) -> Note:
        """Add a new note and return it."""
        next_id = self.notes[-1].id + 1 if self.notes else 1
        note = Note(id=next_id, title=title, content=content, tags=tags or [])
        self.notes.append(note)
        self._save()
        return note

    def list(self) -> List[Note]:
        """Return all notes."""
        return list(self.notes)

    def search(self, keyword: str) -> List[Note]:
        """Return notes that contain keyword in title, content or tags."""
        keyword = keyword.lower()
        result = []
        for note in self.notes:
            if (
                keyword in note.title.lower()
                or keyword in note.content.lower()
                or any(keyword in tag.lower() for tag in note.tags)
            ):
                result.append(note)
        return result

    def remove(self, note_id: int) -> None:
        """Remove a note by its id."""
        self.notes = [n for n in self.notes if n.id != note_id]
        self._save()
