from htmlnode import ParentNode,LeafNode,HTMLNode
from textnode import TextNode,TextType
from text_to_html import text_node_to_html_node
import unittest


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_italic_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code_text(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("cat", TextType.IMAGE,"cat.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"],"cat.png")
        self.assertEqual(html_node.props["alt"], "cat")
    
    def test_link(self):
        node = TextNode("click here", TextType.LINK,"https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"click here")
        self.assertEqual(html_node.props["href"],"https://www.boot.dev")

    def test_invalid_type(self):
        node = TextNode("this is a text node",None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

        
if __name__ == "__main__":
    unittest.main()
