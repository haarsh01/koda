from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from typing import List


class QdrantStore:
    def __init__(self, url: str, api_key: str, collection_name: str):
        self.client = QdrantClient(url=url, api_key=api_key)
        self.collection_name = collection_name

    def create_collection(self, vector_size: int):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

    def upsert(self, vectors: List[List[float]], payloads: List[dict]):
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                (i, vectors[i], payloads[i])
                for i in range(len(vectors))
            ],
        )