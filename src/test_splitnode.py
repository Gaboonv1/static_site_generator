import unittest
from src.splitnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes    
from src.textnode import TextNode, TextType



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

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
def test_multiple_images(self):
    text = "![img1](url1.png) text ![img2](url2.jpg)"
    matches = extract_markdown_images(text)
    self.assertListEqual([("img1", "url1.png"), ("img2", "url2.jpg")], matches)

def test_empty_alt_text(self):
    text = "Check this out: ![](https://example.com)"
    matches = extract_markdown_images(text)
    self.assertListEqual([("", "https://example.com")], matches)

def test_ignore_standard_markdown_links(self):
    text = "This is a [link](https://google.com) and not an image."
    matches = extract_markdown_images(text)
    self.assertListEqual([], matches)

def test_no_images_present(self):
    text = "Just plain old text with no links or images."
    matches = extract_markdown_images(text)
    self.assertListEqual([], matches)

def test_broken_or_incomplete_markdown(self):
    text = "![broken alt(https://example.com) or ![alt](https://fail.com"
    matches = extract_markdown_images(text)
    self.assertListEqual([], matches)

def test_url_with_query_parameters(self):
    text = "![graph](https://api.com)"
    matches = extract_markdown_images(text)
    self.assertListEqual([("graph", "https://api.com")], matches)

def test_split_image_single(self):
    # image only, no surrounding text
    node = TextNode(
        "![cat](https://example.com/cat.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
        ],
        new_nodes,
    )

def test_split_images_multiple(self):
    # two images with text between and before
    node = TextNode(
        "Start ![dog](https://example.com/dog.png) middle ![cat](https://example.com/cat.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("Start ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "https://example.com/dog.png"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
        ],
        new_nodes,
    )

def test_split_image_no_images(self):
    # no images, node should pass through unchanged
    node = TextNode("Just plain text", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)

def test_split_links_multiple(self):
    # two links with trailing text
    node = TextNode(
        "Visit [boot.dev](https://boot.dev) and [youtube](https://youtube.com) for more",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("Visit ", TextType.TEXT),
            TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("youtube", TextType.LINK, "https://youtube.com"),
            TextNode(" for more", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_link_no_links(self):
    # no links, node should pass through unchanged
    node = TextNode("Just plain text", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    self.assertListEqual([node], new_nodes)

def test_split_non_text_node_passes_through(self):
    # non-TEXT nodes should pass through untouched
    node = TextNode("already an image", TextType.IMAGE, "https://example.com/img.png")
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)



if __name__ == "__main__":
    unittest.main()