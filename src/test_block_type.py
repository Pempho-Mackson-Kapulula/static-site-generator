import unittest
from block_type import block_to_block_type,BlockType

class TestBlockTye(unittest.TestCase):
    def test_heading_basic(self):
        self.assertEqual(block_to_block_type("# Heading"),BlockType.HEADING)
        
    def test_invalid_heading_missing_space(self):
        self.assertEqual(block_to_block_type("###Heading"),BlockType.PARAGRAPH)
        
    def test_ordered_list_basic(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"),BlockType.ORDERED_LIST)
        
    def test_ordered_list_broken_sequence(self):
        self.assertEqual(block_to_block_type("1. First\n3. Third\n4. Fourth"),BlockType.PARAGRAPH)
    
    def test_ordered_list_invalid_prefix(self):
        self.assertEqual(block_to_block_type("1. First\n2 Second\n3. Third"),BlockType.PARAGRAPH)
        
    def test_whitespace_only_block(self):
        self.assertEqual(block_to_block_type("   \n   "),BlockType.PARAGRAPH)
        
    


   
        








if __name__ == "__main__":
    unittest.main()