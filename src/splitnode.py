from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
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
    return new_nodes


def extract_markdown_images(text):
    pattern  = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
     new_nodes = []
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue    
        remaining_text = node.text
        for alt, url in images:
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]
        if remaining_text:   
            new_nodes.append(TextNode(remaining_text, TextType.TEXT)) 
     return new_nodes            

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
     new_nodes = []
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue    
        remaining_text = node.text
        for anchor, url in links:
            sections = remaining_text.split(f"[{anchor}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            remaining_text = sections[1]
        if remaining_text:   
            new_nodes.append(TextNode(remaining_text, TextType.TEXT)) 
     return new_nodes    

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)],"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


