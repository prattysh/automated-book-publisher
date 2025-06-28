import chromadb
from chromadb.config import Settings

def save_to_chroma(doc_id, text):
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    collection = client.get_or_create_collection("chapters")

    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[{"source": "AI+Human Final"}]
    )

def retrieve_from_chroma(query):
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    collection = client.get_or_create_collection("chapters")
    results = collection.query(query_texts=[query], n_results=1)
    return results["documents"][0]
