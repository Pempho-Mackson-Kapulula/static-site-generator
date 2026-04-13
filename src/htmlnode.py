

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
    

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag=tag,value=value,children=None,props=props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("Leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,value=None,children=children,props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        
        if self.children is None:
            raise ValueError("Parent nodes must have a child tag")

        inner_html = []
        for child in self.children:
            inner_html.append(child.to_html())

        inner_html = "".join(inner_html)

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
