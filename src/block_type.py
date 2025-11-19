class BlockType(enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unorders_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if len(markodown.lstrip("#")) > 0:
        return BlockType.HEADING

    if markdown[-3:] == markdown[:3]:
        return BlcokType.CODE