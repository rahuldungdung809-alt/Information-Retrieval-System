from normalizer import normalize


def search(query: str, index: dict[str, list[int]], all_doc_ids: list[int]) -> list[int]:
    """Process a small left-to-right Boolean query using AND, OR, and NOT.

    Examples: ``dictionary AND postings``, ``wildcard OR soundex``, and
    ``index NOT positional``. Words without an operator are treated as AND.
    """
    tokens = normalize(query)
    if not tokens:
        return []
    operators = {"and", "or", "not"}
    first_term = next((token for token in tokens if token not in operators), None)
    if first_term is None:
        return []
    result = set(index.get(first_term, []))
    operator = "and"
    first_seen = False
    for token in tokens:
        if token in operators:
            operator = token
            continue
        if not first_seen:
            first_seen = True
            continue
        postings = set(index.get(token, []))
        if operator == "or":
            result |= postings
        elif operator == "not":
            result -= postings
        else:
            result &= postings
        operator = "and"
    return sorted(result)
