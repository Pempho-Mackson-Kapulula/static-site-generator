from block_splitter import markdown_to_blocks
import  unittest

class TestBlockSplitter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_multiple_blank_lines(self):
        md = "A\n\n\n\nB"
        self.assertEqual(
            markdown_to_blocks(md),
            ["A", "B"],
        )
    
    def test_leading_trailing_newlines(self):
        md = "\n\nA\n\nB\n\n"
        self.assertEqual(
            markdown_to_blocks(md),
            ["A", "B"],
        )

    def test_whitespace_only_blocks(self):
        md = "A\n\n   \n\nB"
        self.assertEqual(
            markdown_to_blocks(md),
            ["A", "B"],
        )


if __name__ == "__main__":
    unittest.main()