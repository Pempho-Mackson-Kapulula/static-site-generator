

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        """Render this node as HTML. Must be implemented by subclasses."""
        raise NotImplementedError
    
    def props_to_html(self):
        key_values = []

        for key,value in self.props.items():
            key_values.append(f'{key}="{value}"')

        return " " + " ".join(key_values) if key_values else ""
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"