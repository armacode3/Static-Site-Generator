from textnode import TextNode, TextType

if __name__ == '__main__':
    # plain text
    print(TextNode("Hello world", TextType.TEXT))

    # link
    print(TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"))

    # bold
    print(TextNode("Be bold", TextType.BOLD))
