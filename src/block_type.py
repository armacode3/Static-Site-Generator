from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    match = re.match(r"^(#+)\s", markdown)
    if match is not None:
        if 1 <= len(match.group(1)) <= 6:
            return BlockType.HEADING

    if len(markdown) >= 6:
        if markdown.startswith("```") and markdown.endswith("```"):
            return BlockType.CODE
    
    lines = markdown.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    for i, line in enumerate(lines):
        expected_number = i + 1
        expected_prefix = f"{expected_number}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

    