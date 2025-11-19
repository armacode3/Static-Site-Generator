from extract_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        text = node.text

        extracted_images= extract_markdown_images(text)

        if not extracted_images:
            node_list.append(node)
            continue
        
        for extracted in extracted_images:
            markdown = f"![{extracted[0]}]({extracted[1]})"
            before, after = text.split(markdown, 1)

            if before:
                node_list.append(TextNode(before, TextType.TEXT))
            node_list.append(TextNode(extracted[0], TextType.IMAGE, extracted[1]))
            
            text = after
        
        if text:
            node_list.append(TextNode(text, TextType.TEXT))
    return node_list


def split_nodes_link(old_nodes):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        text = node.text

        extracted_links= extract_markdown_links(text)

        if not extracted_links:
            node_list.append(node)
            continue
        
        for extracted in extracted_links:
            markdown = f"[{extracted[0]}]({extracted[1]})"
            before, after = text.split(markdown, 1)

            if before:
                node_list.append(TextNode(before, TextType.TEXT))
            node_list.append(TextNode(extracted[0], TextType.LINK, extracted[1]))
            
            text = after
        
        if text:
            node_list.append(TextNode(text, TextType.TEXT))
    return node_list