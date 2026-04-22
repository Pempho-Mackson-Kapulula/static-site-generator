from block_splitter import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from htmlnode import ParentNode
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):    
    blocks = markdown_to_blocks(markdown)    
    children = []

    for block in blocks:
        b_type = block_to_block_type(block)

        if b_type == BlockType.PARAGRAPH:
            clean_text = "\n".join(line.strip() for line in block.split("\n"))
            clean_text = clean_text.replace("\n", " ")

            text_nodes = text_to_textnodes(clean_text)

            html_children = [
                text_node_to_html_node(node) for node in text_nodes
            ]

            children.append(ParentNode("p", html_children))
        
        elif b_type == BlockType.HEADING:
            level = 0
            while level < len(block) and block[level] == "#":
                level += 1
            text = block[level + 1:].strip()
            text_nodes = text_to_textnodes(text)
            html_children = [
                text_node_to_html_node(node) for node in text_nodes
            ]
            children.append(ParentNode(f"h{level}", html_children))

        elif b_type == BlockType.CODE:
            lines = block.split("\n")
            if lines[0].strip().startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip().startswith("```"):
                lines = lines[:-1]
                
            cleaned_lines = [line.lstrip() for line in lines]

            text = "\n".join(cleaned_lines)

            if not text.endswith("\n"):
                text += "\n"

            code_node = text_node_to_html_node(
                TextNode(text, TextType.CODE)
            )

            children.append(ParentNode("pre", [code_node]))

     
        elif b_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = " ".join(line.lstrip(">").strip() for line in lines)
            text_nodes = text_to_textnodes(cleaned)
            html_children = [
                text_node_to_html_node(node) for node in text_nodes
            ]

            children.append(ParentNode("blockquote", html_children))

        elif b_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line.lstrip("-").strip()

                text_nodes = text_to_textnodes(text)

                html_children = [
                    text_node_to_html_node(node) for node in text_nodes
                ]

                items.append(ParentNode("li", html_children))

            children.append(ParentNode("ul", items))

        elif b_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line.split(". ", 1)[1]

                text_nodes = text_to_textnodes(text)

                html_children = [
                    text_node_to_html_node(node) for node in text_nodes
                ]
                items.append(ParentNode("li", html_children))
            children.append(ParentNode("ol", items))

    return ParentNode("div", children)