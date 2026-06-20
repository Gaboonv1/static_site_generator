from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node, TextType
from splitnode import text_to_textnodes

def markdown_to_blocks(markdown):
    cleaned_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        cleaned =  block.strip()
        if len(cleaned) != 0:
            cleaned_blocks.append(cleaned)
    return cleaned_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    heading_prefixes = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    lines = block.split("\n")
    if block.startswith(heading_prefixes):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE        
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
            count+=1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    html_nodes = []
    texts = text_to_textnodes(text)
    for text in texts:
        new_nodes = text_node_to_html_node(text)
        html_nodes.append(new_nodes)
    return html_nodes    

def paragraph_to_html_node(block):
    line = block.split("\n")
    new_line = " ".join(line)
    children = text_to_children(new_line)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    block = block[level+1:]
    children = text_to_children(block)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    block = block[3:-3]
    code_text = TextNode(block, TextType.TEXT)
    child = text_node_to_html_node(code_text)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    block = block.split("\n")
    new_lines = []
    for item in block:
        result = item.lstrip(">").strip()
        new_lines.append(result)
    line = " ".join(new_lines)
    child = text_to_children(line)
    return ParentNode("blockquote", child)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        child = text_to_children(text)
        html_items.append(ParentNode("li", child))
    return ParentNode("ul", html_items)    

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for i in items:
        parts = i.split(". ", 1)
        text = parts[1]
        child = text_to_children(text)
        html_items.append(ParentNode("li", child))
    return ParentNode("ol", html_items)    


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNLIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_block = []
    for block in blocks:
        item = block_to_html_node(block)
        new_block.append(item)
    return ParentNode("div", new_block)
       
