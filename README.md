# Spot Access Helper

Spot Access Helper is a Retrieval-Augmented Generation (RAG) system designed to provide intelligent query responses using OpenAI embeddings and Chroma as the vector database. It features a modern web interface built with Flask.

## Features
- File ingestion and parsing.
- Embedding generation and storage in ChromaDB.
- Query and retrieval logic with filtering and pagination.
- Mocked LLM responses for intelligent answers.
- Modern, minimalistic web interface.

## Prerequisites
1. **Python**: Ensure Python 3.8 or later is installed.
2. **Dependencies**: Install required Python packages.
3. **OpenAI API Key**: Obtain an API key from OpenAI (optional for real embeddings).

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd spot-access-helper
```

### Step 2: Set Up Python Environment
Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Application
Edit the `config.py` file to set up your environment variables, including the OpenAI API key (if available).

## Running the Application

### Step 1: Start the Flask Server
Run the following command to start the Flask server:
```bash
python src/app.py
```

### Step 2: Access the Web Interface
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## File Structure
```
spot-access-helper/
├── src/
│   ├── config.py
│   ├── file_parser.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── main.py
│   ├── query_retrieval.py
│   ├── llm.py
│   ├── app.py
├── templates/
│   ├── index.html
├── static/
│   ├── styles.css
│   ├── script.js
├── tests/
│   ├── test_file_parser.py
│   ├── test_query_retrieval.py
│   ├── test_retrieval_accuracy.py
│   ├── test_performance.py
│   ├── test_app.py
│   ├── test_advanced_query.py
├── requirements.txt
├── README.md
```

## Development Workflow

### Step 1: Run Tests
Use `pytest` to run all tests:
```bash
pytest
```

### Step 2: Debugging
Check logs and errors in the terminal to debug issues.

### Step 3: Modify Code
Edit files in the `src/` directory to add or update features.

## Deployment

### Step 1: Prepare for Deployment
Ensure all tests pass and the application runs locally.

### Step 2: Deploy to a Server
Use a platform like AWS, Heroku, or DigitalOcean to deploy the Flask app.

### Step 3: Configure Environment Variables
Set up environment variables on the server for production.

## Troubleshooting

### Common Issues
1. **Dependency Errors**: Ensure all packages are installed using `pip install -r requirements.txt`.
2. **API Key Missing**: Add your OpenAI API key to `config.py`.
3. **Server Not Starting**: Check for syntax errors or missing files.

### Debugging Tips
- Use `print` statements or logging for debugging.
- Check the terminal output for error messages.

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.
