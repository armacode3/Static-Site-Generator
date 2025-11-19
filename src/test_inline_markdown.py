import unittest
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_eq(self):
        nodes = text_to_textnodes("Hello World")
        self.assertEqual(nodes, [TextNode("Hello World", TextType.TEXT)],)