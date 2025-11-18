import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        testNode = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(testNode.to_html(), "<p>This is a paragraph of text.</p>")

        testNode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(testNode.to_html(), '<a href="https://www.google.com">Click me!</a>')

        testNode = LeafNode("p", "Hello, world!")
        self.assertEqual(testNode.to_html(), "<p>Hello, world!</p>")