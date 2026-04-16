import unittest
from textnode import TextNode,TextType
from text_to_textnodes import text_to_textnodes

class TestTextToNode(unittest.TestCase):
    def test_text_to_textnode_split(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

   
    def test_plain_text_only(self):
        text = "Just plain text with nothing special"

        result = text_to_textnodes(text)

        expected = [
            TextNode("Just plain text with nothing special", TextType.TEXT)
        ]

        self.assertEqual(result, expected)


    def test_multiple_bold(self):
        text = "This **bold** and this **also bold** text"

        result = text_to_textnodes(text)

        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_mixed_markdown(self):
        text = "**bold** text with a [link](https://boot.dev) and ![img](https://i.imgur.com/fJRm4Vk.jpeg)"

        result = text_to_textnodes(text)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()