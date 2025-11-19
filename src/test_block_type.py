import unittest

from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_eq(self):
        markdown = "# Title"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.HEADING)

        markdown = "###### Tiny"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.HEADING)

        markdown = "####### Too many"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        markdown = "```\nprint('hi')\n```"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.CODE)

        markdown = "> wisdom"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.QUOTE)

        markdown = "> line1\n> line2"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.QUOTE)

        markdown = "- a\n- b\n- c"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

        markdown = "1. one\n2. two\n3. three"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

        markdown = "1. one\n3. three"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        markdown = "Just a normal paragraph."
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.PARAGRAPH)