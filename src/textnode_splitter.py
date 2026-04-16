from textnode import TextNode,TextType
from markdown_extractor import extract_markdown_images,extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue
            
        remaining = text
        for alt, url in images:
            parts = remaining.split(f"![{alt}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining = parts[1]
            
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue
            
        remaining = text
        for anchor, url in links:
            parts = remaining.split(f"[{anchor}]({url})", 1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
        
            remaining = parts[1]
            
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
            
    return new_nodes