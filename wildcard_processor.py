import re


def wildcard_search(pattern: str, index: dict[str, list[int]]) -> list[int]:
    """Match * against dictionary terms, then combine their document lists."""
    expression = re.compile("^" + re.escape(pattern.lower()).replace(r"\*", ".*") + "$")
    return sorted({doc for term, ids in index.items() if expression.match(term) for doc in ids})
