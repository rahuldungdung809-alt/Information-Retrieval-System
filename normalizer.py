from tokenizer import tokenize


def normalize(text: str) -> list[str]:
    """Case-fold and tokenize so documents and queries use the same form."""
    return [word.lower() for word in tokenize(text)]
