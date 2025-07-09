import unittest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.client = app.test_client()

    def test_query_endpoint(self):
        """Test the /query endpoint with a valid query."""
        response = self.client.post('/query', json={"query": "test document", "top_n": 2})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)
        self.assertTrue("Here is the information you requested" in data["response"])

    def test_empty_query(self):
        """Test the /query endpoint with an empty query."""
        response = self.client.post('/query', json={"query": "", "top_n": 2})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["response"], "No relevant data found.")

if __name__ == "__main__":
    unittest.main()
