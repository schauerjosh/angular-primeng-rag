import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
from src.query_retrieval import query_vector_store
from src.llm import generate_response
from src.vector_store import initialize_chroma, add_to_chroma
from src.embedding import generate_embeddings
from src.file_parser import parse_files

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), '../static'), static_url_path='/static', template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

# Initialize Chroma database with real data from helper-files
chroma_client = initialize_chroma()
helper_files_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../helper-files")
parsed_data = parse_files(helper_files_directory)
text_chunks = [data["text"] for data in parsed_data]
metadata = [{"file_name": data["file_name"], "text": data["text"]} for data in parsed_data]
embeddings = generate_embeddings(text_chunks)
add_to_chroma(chroma_client, embeddings, metadata)

@app.route('/')
def home():
    """Render the main web interface."""
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    """Endpoint to handle user queries with filtering and pagination."""
    data = request.json
    query_text = data.get('query', '')
    top_n = data.get('top_n', 5)
    filters = data.get('filters', None)
    page = data.get('page', 1)
    page_size = data.get('page_size', 10)

    # Retrieve relevant data
    retrieved_data = query_vector_store(query_text, top_n, filters, page, page_size)

    # Generate response using the LLM
    response = generate_response(retrieved_data, query_text)

    return jsonify({"response": response})

@app.route('/test', methods=['GET'])
def test():
    """Render the test template for debugging."""
    return jsonify({"message": "Test route is working!"}), 200

if __name__ == '__main__':
    app.run(port=5003)
