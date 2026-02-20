import requests
from bs4 import BeautifulSoup
from typing import List


def scrape_url(url: str) -> List[str]:
    """
    Fetches a URL and extracts clean paragraph text.
    Returns a list of text blocks.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove noise
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    paragraphs = []
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 50:  # ignore junk
            paragraphs.append(text)

    return paragraphs