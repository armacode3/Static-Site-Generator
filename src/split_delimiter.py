from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []

    if not old_nodes:
        return []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        
        text_list = node.text.split(delimiter)

        if len(text_list) % 2 != 1:
            raise Exception("Invalid delimiter")
        
        for i in range(len(text_list)):
            if text_list[i] == "":
                continue

            if i % 2 == 0:
                node_list.append(TextNode(text_list[i], TextType.TEXT))
            else:
                node_list.append(TextNode(text_list[i], text_type))

    return node_list

        
        