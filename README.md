# Ateismos Study Library

This repository contains a simple Python library for managing study notes.

## Usage

```
from studylib import StudyLibrary

library = StudyLibrary()  # by default uses 'notes.json'
library.add("First Note", "This is an example note.")
all_notes = library.list()
search_results = library.search("example")
```

Notes are stored in a JSON file which is automatically created in the current directory.
