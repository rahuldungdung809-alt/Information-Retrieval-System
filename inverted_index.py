from collections import defaultdict
from document_loader import load_documents
from normalizer import normalize


def build_index(folder: str):
    documents = load_documents(folder)
    index = defaultdict(set)
    for doc_id, (_, text) in documents.items():
        for term in normalize(text): index[term].add(doc_id)
    return documents, {term: sorted(ids) for term, ids in index.items()}
