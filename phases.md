# RAG System Project: Phased Implementation Design

## General Completion Criteria for All Phases
- No phase is considered complete until:
  - All placeholder or dummy code is removed.
  - All components are integrated and tested together (no standalone/test-only code left).
  - A full build and run is performed to ensure there are no errors.
  - Each phase delivers a working, testable POC for its scope.

---

## Phase 1: Core Data Ingestion & Vector Store Setup
### Goals
- Set up the Python project structure.
- Implement file reading and parsing for `/helper-files`.
- Extract relevant data (text, metadata) from supported file types.
- Generate embeddings using OpenAI API (key from `open_ai_key` env variable).
- Store embeddings and metadata in Chroma vector database.

### Implementation Details
- **Project Structure:**
  - Use a `src/` directory for main code, `tests/` for tests.
  - Create a config file or use environment variables for settings (e.g., OpenAI key, Chroma DB path).
- **File Parsing:**
  - Support at least `.txt`, `.md`, and optionally `.pdf` (using PyPDF2 or similar).
  - Implement chunking for large files (e.g., 500-1000 tokens per chunk).
  - Extract and store metadata (filename, chunk index, etc.).
- **Embedding Generation:**
  - Use OpenAI’s embedding endpoint directly (no Langchain).
  - Handle API errors and rate limits gracefully.
- **Chroma Integration:**
  - Store each chunk as a document with its embedding and metadata.
  - Provide functions to add, update, and search documents.
- **Testing:**
  - Unit tests for file parsing and embedding functions.
  - Integration test: ingest a file, store in Chroma, and retrieve by vector search.

---

## Phase 2: Query & Retrieval Logic
### Goals
- Implement query interface to accept user questions.
- Embed queries and retrieve relevant chunks from Chroma.

### Implementation Details
- **Query Embedding:**
  - Use the same OpenAI embedding model as for documents.
- **Vector Search:**
  - Retrieve top-N most similar chunks (configurable N).
  - Return both text and metadata for each result.
- **Testing:**
  - Test with sample queries to ensure relevant results are returned.
  - Validate retrieval accuracy and performance.

---

## Phase 3: LLM Integration for RAG
### Goals
- Integrate OpenAI LLM to answer questions using retrieved context.

### Implementation Details
- **Prompt Construction:**
  - Concatenate retrieved chunks and user query into a prompt.
  - Optionally, add system instructions for the LLM.
- **LLM Call:**
  - Use OpenAI’s chat/completions endpoint.
  - Handle token limits (truncate context if needed).
- **Testing:**
  - End-to-end test: user query → retrieval → LLM answer.
  - Validate that answers use context from the vector store.

---

## Phase 4: Flask Web Interface
### Goals
- Build a web-based chat interface for user interaction.

### Implementation Details
- **Flask App:**
  - Set up Flask with routes for chat and static files.
  - Use a simple HTML/JS frontend (e.g., Bootstrap for styling).
- **Backend Integration:**
  - Connect Flask endpoints to the RAG pipeline (query, retrieve, answer).
  - Maintain session state for chat history.
- **Testing:**
  - Manual and automated tests for the web UI.
  - End-to-end test: user interacts via web, receives LLM answers with context.

---

## Phase 5: Usability, Error Handling, and Enhancements
### Goals
- Improve robustness, usability, and feature set.

### Implementation Details
- **Error Handling:**
  - Add user-friendly error messages and logging.
  - Handle file parsing, API, and DB errors gracefully.
- **Enhancements:**
  - Support more file types (e.g., .docx, .csv).
  - Add file re-indexing and update capabilities.
  - Optional: user authentication, chat history export, etc.
- **Testing:**
  - Test all new features and error cases.
  - Regression test to ensure previous functionality is intact.

---

## Phase 6: Final Testing & Documentation
### Goals
- Ensure system is production-ready and well-documented.

### Implementation Details
- **Testing:**
  - Comprehensive unit, integration, and manual tests.
  - Test with real-world files and queries.
- **Documentation:**
  - Write setup, usage, and maintenance docs.
  - Document API endpoints, configuration, and troubleshooting.
- **Final Review:**
  - Double-check for any remaining placeholder code or incomplete integration.
  - Perform a final build and run to confirm error-free operation.

---

**Note:**
- Each phase must be fully integrated and tested before moving to the next.
- No phase is complete until all placeholder code is removed, all components are working together, and a full build passes without errors.
