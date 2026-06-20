import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_values(self):
        node = HTMLNode(
            "div",
            "I am a div",
            None,
            {"class": "greeting", "id": "main"}
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I am a div")

    def test_children_initialization(self):
        child1 = HTMLNode("b", "Bold text")
        child2 = HTMLNode("i", "Italic text")
        parent = HTMLNode("p", None, [child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].tag, "b")

    def mutliple_props(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')

    def no_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
            


if __name__ == "__main__":
    unittest.main()