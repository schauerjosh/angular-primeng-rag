import unittest
import sys
import os
from PyPDF2 import PdfWriter, PageObject
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from file_parser import parse_files

class TestFileParser(unittest.TestCase):

    def setUp(self):
        """Set up a temporary directory with test files."""
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)
        pdf_writer = PdfWriter()
        page = PageObject.create_blank_page(width=300, height=300)
        pdf_writer.add_page(page)
        with open(os.path.join(self.test_dir, "test1.pdf"), "wb") as f:
            pdf_writer.write(f)

    def tearDown(self):
        """Clean up the temporary directory."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_parse_files(self):
        """Test the parse_files function."""
        parsed_data = parse_files(self.test_dir)
        self.assertEqual(len(parsed_data), 1)
        self.assertEqual(parsed_data[0]["file_name"], "test1.pdf")
        self.assertTrue(parsed_data[0]["text"])

if __name__ == "__main__":
    unittest.main()
