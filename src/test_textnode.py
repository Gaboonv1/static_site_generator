import unittest
from src.textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
   
    def test_not_eq(self):
        node =  TextNode("This is a text node", TextType.BOLD)  
        node2 = TextNode("This is a text node", TextType.ITALIC) 
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node =  TextNode("This is a text node", TextType.BOLD)  
        node2 = TextNode("Hello world", TextType.ITALIC) 
        self.assertNotEqual(node, node2)

    def test_url(self):
        node =  TextNode("This is a text node", TextType.BOLD, url="https://example.com")  
        node2 = TextNode("Hello world", TextType.BOLD, url = None) 
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")    

    def test_text_node_to_html_node_image(self):
        node = TextNode("An alt text description", TextType.IMAGE, "https://boot.dev/logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://boot.dev/logo.png", "alt": "An alt text description"},
        )    

    def test_text_node_to_html_node_invalid(self):
        node = TextNode("invalid node", "some_fake_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)



if __name__ == "__main__":
    unittest.main()