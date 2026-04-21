from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    expected = 1
    for line in lines:
        parts = line.split(". ", 1)
        if len(parts) != 2:
            break

        number_str, _ = parts

        if not number_str.isdigit():
            break

        if int(number_str) != expected:
            break

        expected += 1
    else:
        return BlockType.ORDERED_LIST

    if line_starts_as_heading(block):
        return BlockType.HEADING

    return BlockType.PARAGRAPH


def line_starts_as_heading(block):
    first_line = block.split("\n")[0]

    if not first_line.startswith("#"):
        return False

    i = 0
    while i < len(first_line) and first_line[i] == "#":
        i += 1

    if i == 0 or i > 6:
        return False

    if i >= len(first_line):
        return False

    return first_line[i] == " "