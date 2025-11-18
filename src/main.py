from textnode import TextNode, TextType

from split_delimiter import split_nodes_delimiter

if __name__ == '__main__':
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
