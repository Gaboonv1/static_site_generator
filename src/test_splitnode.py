import unittest
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextType



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)


def test_code_delimiter(self):
    node = TextNode("This is `code` here", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(result, [
        TextNode("This is ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" here", TextType.TEXT),
    ])


def test_invalid_markdown(self):
    node = TextNode("This is `unclosed", TextType.TEXT)
    with self.assertRaises(ValueError):
        split_nodes_delimiter([node], "`", TextType.CODE)


        






if __name__ == "__main__":
    unittest.main()