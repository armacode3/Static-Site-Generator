from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None and self.tag != "img":
            raise ValueError(f"All leaf nodes must have a value. Tag: {self.tag}")
        
        if self.tag is None:
            return f"{self.value}"
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        combined_props = self.props_to_html()

        if self.tag == "img":
            return f"<{self.tag}{combined_props}>"

        return f"<{self.tag}{combined_props}>{self.value}</{self.tag}>"