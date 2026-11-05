
# Information Retrieval / Web Search Mining

A Python-based Information Retrieval System with a native Tkinter desktop GUI, developed for a university viva.

The application demonstrates fundamental concepts of Information Retrieval, including document loading, tokenization, case folding, inverted indexing, Boolean query processing, and wildcard searching.

## Features

- **Document Loading:** Reads plain-text lecture notes.
- **Tokenization:** Splits documents into individual words.
- **Case Folding:** Converts terms into a consistent lowercase format.
- **Inverted Indexing:** Maps terms to the documents in which they appear.
- **Boolean Search:** Supports AND, OR, and NOT queries.
- **Wildcard Search:** Supports searches using the `*` wildcard.
- **Desktop GUI:** Provides a search box, Search button, read-only results area, and lecture-based concept explanations.

## Technologies Used

- Python
- Tkinter
- Regular Expressions
- Pytest

## Project Structure

```text
Information-Retrieval-System/
│
├── data/
│   └── lecture_corpus/
│
├── document_loader.py
├── tokenizer.py
├── normalizer.py
├── inverted_index.py
├── query_processor.py
├── wildcard_processor.py
├── gui.py
├── run.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rahuldungdung809-alt/Information-Retrieval-System.git
cd Information-Retrieval-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python run.py
```

## Running Tests

Run the following command:

```bash
pytest
```

## Project Modules

| File | Description |
|---|---|
| `document_loader.py` | Loads plain-text lecture notes. |
| `tokenizer.py` | Splits text into words. |
| `normalizer.py` | Case-folds document and query terms. |
| `inverted_index.py` | Builds the term-to-document mapping. |
| `query_processor.py` | Processes AND, OR, and NOT Boolean queries. |
| `wildcard_processor.py` | Resolves wildcard searches. |
| `gui.py` | Implements the Tkinter desktop interface. |
| `run.py` | Starts the application. |

## Lecture Corpus

The project contains 51 separate lecture notes derived from three supplied lectures.

It also includes a Westlaw Boolean-search example based on the introductory lecture.

## Implementation Note

The inverted index is maintained in memory. If a document in the corpus is modified, restart the application to load the updated content.

## Author

**Rahul Dungdung**

GitHub: [rahuldungdung809-alt](https://github.com/rahuldungdung809-alt)
