from textnode import TextNode,TextType
from htmlnode import HTMLNode,ParentNode,LeafNode

def text_node_to_html_node(text_node):
    t = text_node.text_type

    if t == TextType.TEXT:
        return LeafNode(None,text_node.text)
    
    if t == TextType.BOLD:
        return LeafNode("b",text_node.text)
    
    if t == TextType.ITALIC:
        return LeafNode("i",text_node.text)
    
    if t == TextType.CODE:
        return LeafNode("code",text_node.text)
    
    if t == TextType.LINK:
        return LeafNode("a",text_node.text,{"href": text_node.url})
    
    if t == TextType.IMAGE:
        return LeafNode("img","",{"alt":text_node.text,"src":text_node.url})
    
    raise ValueError("Unsupported TextType")
