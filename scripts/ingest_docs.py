import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from backend.ingestion.scraper import scrape_url
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedder import Embedder
from backend.vectorstore.qdrant import QdrantStore

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

COLLECTION_NAME = "koda_docs"


def main():
    url = "https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html"

    print("Scraping...")
    texts = scrape_url(url)

    print("Chunking...")
    chunks = chunk_text(texts)

    print("Embedding...")
    embedder = Embedder()
    vectors = embedder.embed(chunks)

    print("Storing in Qdrant...")
    store = QdrantStore(QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME)
    store.create_collection(vector_size=len(vectors[0]))

    payloads = [{"text": chunk, "source": url} for chunk in chunks]
    store.upsert(vectors, payloads)

    print("Ingestion complete ")


if __name__ == "__main__":
    main()