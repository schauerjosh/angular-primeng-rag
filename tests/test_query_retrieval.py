import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from query_retrieval import query_vector_store
from vector_store import initialize_chroma, add_to_chroma

class TestQueryRetrieval(unittest.TestCase):

    def setUp(self):
        """Set up a temporary Chroma database with test data."""
        self.chroma_client = initialize_chroma()
        embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        metadata = [{"file_name": "test1.pdf"}, {"file_name": "test2.pdf"}]
        add_to_chroma(self.chroma_client, embeddings, metadata)

    def tearDown(self):
        """Clean up the Chroma database."""
        self.chroma_client.delete_collection(name="rag_collection")

    def test_query_vector_store(self):
        """Test the query_vector_store function."""
        query = "test query"
        results = query_vector_store(query, top_n=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["file_name"], "test1.pdf")

if __name__ == "__main__":
    unittest.main()
