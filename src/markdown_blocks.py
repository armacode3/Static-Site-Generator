

def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")

    clean = []

    for string in markdown_list:
        if string:
            clean.append(string.strip())

    return clean

if __name__ == "__main__":
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
    print(markdown_to_blocks(md))
    print(["This is **bolded** paragraph", "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line", "- This is a list\n- with items"])