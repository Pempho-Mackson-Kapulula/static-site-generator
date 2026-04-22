import unittest
from title_extractor import extract_title

class TestTitleExtractor(unittest.TestCase):
    def test_simple_title(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")
        
    def test_whitespace_title(self):
        md = "   #   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")
        
    def test_title_not_first_line(self):
        md = "\n\n# My Title\nSome text"
        self.assertEqual(extract_title(md), "My Title")
    
    def test_invalid_heading_level(self):
        md = "## Not a title"
        with self.assertRaises(Exception):
            extract_title(md)
    
    def test_no_title(self):
        md = "Just some text\nAnother line"
        with self.assertRaises(Exception):
            extract_title(md)
            
            
if __name__ == "__main__":
    unittest.main()