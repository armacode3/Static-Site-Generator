import re
from parentnode import ParentNode
from markdown_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)  # Split markdown into list of blocks

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        tag = return_tag(block_type, block)

        if block_type == BlockType.PARAGRAPH:
            one_line = " ".join(block.split("\n"))
            children_block = text_to_children(one_line)
            children.append(ParentNode(tag, children_block))

        elif block_type == BlockType.HEADING:
            string = re.sub(r"^#+\s?", "", block)
            children_block = text_to_children(string)
            children.append(ParentNode(tag, children_block))

        elif block_type == BlockType.UNORDERED_LIST:
            children_block = list_block_to_children(block, False)
            children.append(ParentNode(tag, children_block))

        elif block_type == BlockType.ORDERED_LIST:
            children_block = list_block_to_children(block, True)
            children.append(ParentNode(tag, children_block))

        elif block_type == BlockType.QUOTE:
            children_block = quote_block_to_children(block)
            children.append(ParentNode(tag, children_block))

        elif block_type == BlockType.CODE:
            codeNode = code_block_to_children(block)
            children.append(codeNode)
        else:
            raise Exception("Error: Not a Block Type")


    return ParentNode("div", children)


def return_tag(blockType, block):
    if blockType == BlockType.QUOTE:
        return "blockquote"

    if blockType == BlockType.UNORDERED_LIST:
        return "ul"

    if blockType == BlockType.ORDERED_LIST:
        return "ol"

    if blockType == BlockType.CODE:
        return "code"

    if blockType == BlockType.HEADING:
        match = re.match(r"^(#+)\s", block)
        if match:
            return "h" + str(len(match.group(1)))

        raise Exception("No Header")

    if blockType == BlockType.PARAGRAPH:
        return "p"

    raise Exception("Not a Block Type")

def list_block_to_children(block, ordered):
    block_list = block.split("\n")

    list_children = []

    if ordered:
        for line in block_list:
            if line:
                space_index = line.find(" ")
                if space_index != -1:
                    clean_line = line[space_index + 1:]
                else:
                    clean_line = line

                children = text_to_children(clean_line)
                list_children.append(ParentNode("li", children))
    else:
        for line in block_list:
            if line:
                if line.startswith("- "):
                    clean_line = line[2:]
                else:
                    clean_line = line

                children = text_to_children(clean_line)
                list_children.append(ParentNode("li", children))
    return list_children

def text_to_children(text):
    textNodes = text_to_textnodes(text)
    
    htmlNodes = []
    for node in textNodes:
        htmlNodes.append(text_node_to_html_node(node))
    return htmlNodes

def quote_block_to_children(block):
    split_block = block.split("\n")

    final_line = ""

    for line in split_block:
        if not line:
            continue
        if line.startswith("> "):
            clean_line = line[2:]
        else:
            clean_line = line

        final_line += clean_line + "\n"

    textNodes = text_to_children(final_line)
    return textNodes

def code_block_to_children(block):
    block_lines = block.split("\n")
    middle_lines = block_lines[1:-1]

    middle_string = "\n".join(middle_lines) + "\n"


    stringNode = TextNode(middle_string, TextType.CODE)

    code_node = text_node_to_html_node(stringNode)

    return ParentNode("pre", [code_node])



