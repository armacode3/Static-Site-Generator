from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        
        if not self.tag:
            return f"{self.value}"
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        combined_props = self.props_to_html()
        return f"<{self.tag}{combined_props}>{self.value}</{self.tag}>"