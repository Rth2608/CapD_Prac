from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import openai
import os
from dotenv import load_dotenv

load_dotenv()

qdrant = QdrantClient(url=os.getenv("QDRANT_HOST"))
COLLECTION_NAME = "news_summaries"

def init_qdrant_collection():
    if not qdrant.collection_exists(COLLECTION_NAME):
        qdrant.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
        )

def embed_text(text: str):
    response = openai.Embedding.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

def add_news_to_qdrant(news_id: int, summary: str):
    vector = embed_text(summary)
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=news_id, vector=vector, payload={"summary": summary})]
    )

def search_similar_news(query: str, top_k: int = 5):
    vector = embed_text(query)
    search_result = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=top_k
    )
    return [
        {
            "id": item.id,
            "score": item.score,
            "summary": item.payload.get("summary")
        }
        for item in search_result
    ]
