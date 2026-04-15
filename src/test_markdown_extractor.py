import unittest
from markdown_extractor import extract_markdown_images,extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], extract_markdown_links(text))

    def test_multiple_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and this is text with another ![image2](https://www.google.com)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://www.google.com")]
        self.assertListEqual(expected, extract_markdown_images(text))

    def test_extract_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and this is another link [to google](https://www.google.com)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to google", "https://www.google.com")]
        self.assertListEqual(expected, extract_markdown_links(text))

    def test_no_matching_images(self):
        self.assertListEqual([], extract_markdown_images("This is text with no image to extract"))
    
    def test_no_matching_links(self):
        self.assertListEqual([], extract_markdown_links("This is text with no link to extract"))

    def test_empty_string(self):
        self.assertListEqual([], extract_markdown_images(""))
        self.assertListEqual([], extract_markdown_links(""))

    def test_malformed_syntax(self):
        self.assertListEqual([], extract_markdown_links("This is a [link](https://google.com"))
        self.assertListEqual([], extract_markdown_images("![broken link](https://imgur.com/a.png"))
        self.assertListEqual([], extract_markdown_links("Just some [text] and (link)"))
    
    def test_complex_urls(self):
        text = "Check this [link](https://www.example.com/path?query=1&id=2#section)"
        expected = [("link", "https://www.example.com/path?query=1&id=2#section")]
        self.assertListEqual(expected, extract_markdown_links(text))

    def test_mixed_content(self):
        text = "![image](https://example.com/img.png) and [link](https://example.com)"
        self.assertListEqual([("image", "https://example.com/img.png")], extract_markdown_images(text))
        self.assertListEqual([("link", "https://example.com")], extract_markdown_links(text))
    


if __name__ == "__main__":
    unittest.main()