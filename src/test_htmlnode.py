import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

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

    #leaf node test
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Link", props={"href": "https://google.com", "target": "_blank"})
        result = node.to_html()
        self.assertIn('href="https://google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith("<a "))
        self.assertTrue(result.endswith("</a>"))

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    #test parent node
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_single_child(self):
        child = LeafNode("span", "hello")
        node = ParentNode("div", [child])
        self.assertEqual(node.to_html(), "<div><span>hello</span></div>")

    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, "Normal"),
                LeafNode("i", "Italic"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b>Normal<i>Italic</i></p>"
        )

    def test_nested_parent_nodes(self):
        grandchild = LeafNode("b", "deep")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span><b>deep</b></span></div>"
        )

    def test_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [LeafNode(None, "text")]
                        )
                    ],
                )
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<div><section><p>text</p></section></div>"
        )

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "child")],
            {"class": "container", "id": "main"},
        )

        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )
    
    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "test")]).to_html()
    
    def test_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_mixed_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold"),
                ParentNode("span", [LeafNode(None, "inner")]),
                LeafNode(None, "text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<div><b>Bold</b><span>inner</span>text</div>"
        )
if __name__ == "__main__":
    unittest.main()