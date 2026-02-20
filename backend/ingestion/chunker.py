from typing import List


def chunk_text(
    texts: List[str],
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    """
    Splits text into overlapping chunks.
    """
    chunks = []

    for text in texts:
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap

    return chunks