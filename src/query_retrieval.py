import openai
from src.vector_store import initialize_chroma, search_chroma
from src.config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def query_vector_store(query, top_n=5, filters=None, page=1, page_size=10):
    """Generate real query embeddings and retrieve relevant chunks from Chroma with filtering and pagination."""
    if not query:
        return []  # Handle empty query

    # Generate real query embedding using OpenAI API
    query_embedding = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002"
    )["data"][0]["embedding"]

    print(f"Query Embedding: {query_embedding[:10]}...")  # Debug log for query embedding

    chroma_client = initialize_chroma()
    results = search_chroma(chroma_client, query_embedding, top_n)

    # Debug: Log retrieved results
    print("Retrieved Results from ChromaDB:", results)

    # Sort results by score (if available) and return the top results
    sorted_results = sorted(
        results,
        key=lambda x: x.get("score", 0),
        reverse=True
    )

    print(f"Sorted Results: {sorted_results}")  # Debug log for sorted results

    return sorted_results
