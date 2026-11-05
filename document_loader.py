from pathlib import Path


def load_documents(folder: str) -> dict[int, tuple[str, str]]:
    """Read every text file and return {id: (filename, content)}."""
    return {number: (path.name, path.read_text(encoding="utf-8")) for number, path in enumerate(sorted(Path(folder).glob("*.txt")), 1)}
