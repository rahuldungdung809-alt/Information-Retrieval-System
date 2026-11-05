# Information Retrieval / Web Search Mining

A native Tkinter desktop GUI designed for a university viva. It demonstrates document loading, tokenization, case folding, inverted indexing, AND query processing, and wildcard search.

## Run it

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Run `python run.py` to open the desktop GUI. It has a search box, a Search button, a read-only result area, and lecture-based concept explanations.

## Test it

```bash
pytest
```

## Project layout

- `document_loader.py` reads plain-text lecture notes.
- `tokenizer.py` splits text into words.
- `normalizer.py` case-folds query and document terms.
- `inverted_index.py` builds the dictionary-to-document mapping.
- `query_processor.py` supports simple left-to-right `AND`, `OR`, and `NOT` Boolean queries.
- `wildcard_processor.py` resolves `*` wildcard searches.
- `gui.py` contains the native desktop GUI.
- `data/lecture_corpus/` contains 51 separate notes derived from the three supplied lectures.

The corpus also includes a Westlaw Boolean-search example drawn from the introductory lecture.

The index is intentionally held in memory to make source changes in the corpus easy to demonstrate: restart the app after editing a document.
