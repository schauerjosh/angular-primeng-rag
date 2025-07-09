import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from query_retrieval import query_vector_store
from vector_store import initialize_chroma, add_to_chroma

class TestPerformance(unittest.TestCase):

    def setUp(self):
        """Set up a temporary Chroma database with a large dataset."""
        self.chroma_client = initialize_chroma()
        embeddings = [[i * 0.1, i * 0.2, i * 0.3] for i in range(1000)]
        metadata = [
            {"file_name": f"test{i}.pdf", "content": f"This is test document {i}."}
            for i in range(1000)
        ]
        add_to_chroma(self.chroma_client, embeddings, metadata)

    def tearDown(self):
        """Clean up the Chroma database."""
        self.chroma_client.delete_collection(name="rag_collection")

    def test_large_dataset_query(self):
        """Test querying performance with a large dataset."""
        query = "test document"
        results = query_vector_store(query, top_n=10)
        self.assertEqual(len(results), 10)
        self.assertTrue(all("test" in result["file_name"] for result in results))

    def test_multiple_queries(self):
        """Test performance with multiple queries."""
        queries = [f"test document {i}" for i in range(10)]
        for query in queries:
            results = query_vector_store(query, top_n=5)
            self.assertLessEqual(len(results), 5)

if __name__ == "__main__":
    unittest.main()
