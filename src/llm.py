import openai
from src.config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_response(retrieved_data, query):
    """Generate a response using OpenAI's LLM based on retrieved data."""
    if not retrieved_data:
        return "No relevant data found. Please ensure the query is related to the indexed documents."

    # Include more context in the prompt
    context = "\n\n".join([
        f"File: {item['metadata']['file_name']}\nContent: {item['metadata']['content'][:500]}"
        for item in retrieved_data
    ])

    prompt = (
        "You are an expert assistant. Use the context below to answer the user's query. "
        "If the context is insufficient, indicate that more information is needed.\n\n"
        f"Context:\n{context}\n\nUser Query: {query}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"].strip()
