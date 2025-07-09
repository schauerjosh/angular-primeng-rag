import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_parser import parse_files
from embedding import generate_embeddings
from vector_store import initialize_chroma, add_to_chroma, list_chroma_data, list_indexed_embeddings

# Step 1: Parse files from the helper-files directory
helper_files_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../helper-files")
parsed_data = parse_files(helper_files_directory)

# Step 2: Generate embeddings for parsed text chunks
text_chunks = [data["text"] for data in parsed_data]
metadata = [{"file_name": data["file_name"], "text": data["text"]} for data in parsed_data]
embeddings = generate_embeddings(text_chunks)

print(f"Parsed {len(parsed_data)} files.")
print(f"Generated {len(embeddings)} embeddings.")
print(f"Metadata count: {len(metadata)}")

if not embeddings or not metadata:
    print("No embeddings or metadata to add to ChromaDB. Aborting.")
else:
    # Step 3: Store embeddings and metadata in Chroma
    chroma_client = initialize_chroma()
    print("Adding embeddings to ChromaDB...")
    add_to_chroma(chroma_client, embeddings, metadata)
    print("Embeddings added to ChromaDB.")

    # Step 4: Verify stored data in ChromaDB
    def list_chroma_data(chroma_client):
        """List all data stored in the Chroma vector store."""
        collection = chroma_client.get_collection(name="rag_collection")
        data = collection.get(include=["metadatas", "documents", "embeddings"])
        print("Indexed Data in ChromaDB:", data)
        return data

    # Call this function after ingestion
    stored_data = list_chroma_data(chroma_client)
    if not stored_data["documents"]:
        print("No documents found in ChromaDB. Please check the ingestion process.")
    else:
        print(f"Number of documents indexed: {len(stored_data['documents'])}")

    # After ingestion, list all indexed embeddings for debugging
    list_indexed_embeddings(chroma_client)

print("Phase 1 completed successfully!")

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
