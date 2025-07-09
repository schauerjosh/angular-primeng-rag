import unittest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from app import app

class TestAdvancedQuery(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.client = app.test_client()

    def test_query_with_filters(self):
        """Test the /query endpoint with filters."""
        response = self.client.post('/query', json={
            "query": "test document",
            "top_n": 5,
            "filters": {"file_name": "test1.pdf"}
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)
        self.assertTrue("test1.pdf" in data["response"])

    def test_query_with_pagination(self):
        """Test the /query endpoint with pagination."""
        response = self.client.post('/query', json={
            "query": "test document",
            "top_n": 5,
            "page": 1,
            "page_size": 1
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)
        self.assertTrue("test1.pdf" in data["response"])

if __name__ == "__main__":
    unittest.main()
