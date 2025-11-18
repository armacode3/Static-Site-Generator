from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        
        if not self.props:
            combined_string = f"<{self.tag}>"
        else:
            combined_props = self.props_to_html()
            combined_string = f"<{self.tag}{combined_props}>"

        inner = "".join(child.to_html() for child in self.children)

        combined_string += f"{inner}</{self.tag}>"
        return combined_string

        