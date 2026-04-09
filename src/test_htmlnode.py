import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_multiple_props(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://google.com", "target": "_blank"})
        result = node.props_to_html()
        # order in dicts can vary, so test contains both attributes
        self.assertIn('href="https://google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))
    

if __name__ == "__main__":
    unittest.main()