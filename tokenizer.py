import re


def tokenize(text: str) -> list[str]:
    """Split text into alphabetic words."""
    return re.findall(r"[a-zA-Z]+", text)
