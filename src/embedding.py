import openai
from config import OPENAI_API_KEY
from tiktoken import encoding_for_model

def split_text_into_chunks(text, max_tokens):
    """Split text into smaller chunks based on token limit."""
    enc = encoding_for_model("text-embedding-ada-002")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunks.append(enc.decode(chunk_tokens))
    return chunks

def generate_embeddings(text_chunks):
    """Generate embeddings for a list of text chunks using OpenAI API."""
    openai.api_key = OPENAI_API_KEY
    embeddings = []
    max_tokens = 8192  # Model's token limit
    for chunk in text_chunks:
        if len(chunk) > max_tokens:
            sub_chunks = split_text_into_chunks(chunk, max_tokens)
        else:
            sub_chunks = [chunk]
        for sub_chunk in sub_chunks:
            response = openai.Embedding.create(
                input=sub_chunk,
                model="text-embedding-ada-002"
            )
            if any(map(lambda x: x != x, response["data"][0]["embedding"])):
                print(f"Warning: NaN detected in embedding for chunk: {chunk[:30]}...")
                continue
            print(f"Generated embedding for chunk: {sub_chunk[:30]}... -> Dimension: {len(response['data'][0]['embedding'])}")
            embeddings.append(response["data"][0]["embedding"])
    return embeddings
