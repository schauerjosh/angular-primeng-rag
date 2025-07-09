import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from query_retrieval import query_vector_store
from vector_store import initialize_chroma, add_to_chroma

class TestRetrievalAccuracy(unittest.TestCase):

    def setUp(self):
        """Set up a temporary Chroma database with test data."""
        self.chroma_client = initialize_chroma()
        embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
        metadata = [
            {"file_name": "test1.pdf", "content": "This is a test document."},
            {"file_name": "test2.pdf", "content": "Another test document."},
            {"file_name": "test3.pdf", "content": "Yet another test document."}
        ]
        add_to_chroma(self.chroma_client, embeddings, metadata)

    def tearDown(self):
        """Clean up the Chroma database."""
        self.chroma_client.delete_collection(name="rag_collection")

    def test_retrieval_accuracy(self):
        """Test retrieval accuracy for a specific query."""
        query = "test document"
        results = query_vector_store(query, top_n=2)
        self.assertEqual(len(results), 2)
        self.assertIn("test1.pdf", [result["file_name"] for result in results])
        self.assertIn("test2.pdf", [result["file_name"] for result in results])

if __name__ == "__main__":
    unittest.main()
