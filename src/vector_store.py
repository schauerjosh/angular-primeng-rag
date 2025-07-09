import chromadb
from chromadb.config import Settings
from config import CHROMA_DB_PATH
import os

def initialize_chroma():
    """Initialize Chroma vector database."""
    # Ensure the ChromaDB directory exists
    if not os.path.exists(CHROMA_DB_PATH):
        os.makedirs(CHROMA_DB_PATH)
        print(f"Created ChromaDB directory at: {CHROMA_DB_PATH}")
    client = chromadb.Client(Settings(persist_directory=CHROMA_DB_PATH))
    print(f"ChromaDB Client Initialized: {client}")
    print(f"Existing Collections: {client.list_collections()}")
    collection = client.get_or_create_collection(name="rag_collection")
    print(f"Collection Created or Retrieved: {collection}")
    return client

def add_to_chroma(client, embeddings, metadata):
    """Add embeddings and metadata to Chroma."""
    collection = client.get_or_create_collection(name="rag_collection")
    ids = []
    metadatas = []
    all_embeddings = []
    for i, (embedding, meta) in enumerate(zip(embeddings, metadata)):
        unique_id = f"{meta['file_name']}_{i}"
        # Use 'text' if present, else fallback to 'content', else empty string
        text_val = meta.get("text", meta.get("content", ""))
        metadatas.append({**meta, "content": text_val})
        ids.append(unique_id)
        all_embeddings.append(embedding)
    if ids:
        print(f"Adding {len(ids)} embeddings to ChromaDB...")
        try:
            collection.add(embeddings=all_embeddings, metadatas=metadatas, ids=ids)
            print("Successfully added all embeddings to ChromaDB.")
            client.persist()  # Ensure data is written to disk
            print("ChromaDB persisted to disk.")
        except Exception as e:
            print(f"Error adding to ChromaDB: {e}")
    else:
        print("No embeddings to add to ChromaDB.")

def search_chroma(client, query_embedding, top_n=5):
    """Search Chroma for the most relevant embeddings."""
    try:
        collection = client.get_collection(name="rag_collection")
        results = collection.query(query_embeddings=[query_embedding], n_results=top_n)

        print(f"Query Embedding: {query_embedding[:10]}...")  # Debug log for query embedding
        print(f"Raw Results: {results}")  # Debug log for raw results

        # Parse and return results
        parsed_results = []
        metadatas = results.get("metadatas", [[]])
        distances = results.get("distances", [[]])

        for i, metadata_list in enumerate(metadatas):
            for j, metadata in enumerate(metadata_list):
                parsed_results.append({
                    "content": metadata.get("content", "") if isinstance(metadata, dict) else "",
                    "metadata": metadata if isinstance(metadata, dict) else {},
                    "score": distances[i][j] if i < len(distances) and j < len(distances[i]) else None
                })

        print(f"Parsed Results: {parsed_results}")  # Debug log for parsed results
        return parsed_results

    except Exception as e:
        print(f"Error during Chroma search: {e}")
        return []

def list_chroma_data(client):
    """List all data stored in ChromaDB."""
    collection = client.get_collection(name="rag_collection")
    all_data = collection.get()
    print(f"Stored Data in ChromaDB: {all_data}")
    return all_data

def list_indexed_embeddings(client):
    """List all indexed embeddings and their metadata in ChromaDB."""
    try:
        collection = client.get_collection(name="rag_collection")
        results = collection.get()
        print(f"Raw collection.get() output: {results}")  # Debug log

        if not results or not results.get("metadatas"):
            print("No embeddings found in the collection.")
            return

        print("Indexed Embeddings:")
        for metadata, embedding in zip(results.get("metadatas", []), results.get("embeddings", [])):
            print(f"Metadata: {metadata}, Embedding (first 10 values): {embedding[:10]}...")

    except Exception as e:
        print(f"Error listing indexed embeddings: {e}")
