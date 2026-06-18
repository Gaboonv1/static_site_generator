from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node != text_type.Text:
            new_nodes.append(node)
            continue
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise ValueError("invalid markdown text")
            for i, split in enumerate(split_node):
                if split =="":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split, text_type))

def test_invalid_markdown(self):
    node = TextNode("This is `unclosed", TextType.TEXT)
    with self.assertRaises(ValueError):
        split_nodes_delimiter([node], "`", TextType.CODE)


        