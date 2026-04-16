from textnode import TextNode,TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown Syntax: Unclosed Delimiter")

            for i in range(len(parts)):
                if i % 2 == 0:
                    if parts[i] != "":
                        new_nodes.append(TextNode(parts[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(parts[i],text_type))

    return new_nodes