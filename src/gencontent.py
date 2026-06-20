from markdown_blocks import markdown_to_html_node 
from htmlnode import HTMLNode
from pathlib import Path
import os

def extract_title( markdown):
   lines = markdown.split("\n")
   for line in lines:
      if line.startswith("# "):
         result = line[2:]
         break
   else:   
        raise Exception("There are no headers")   
   return result.strip()     

def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path, "r")
    contents = file.read()
    file.close()
    template = open(template_path, "r")
    template_content =  template.read()
    template.close()
    html = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)
    template_content = template_content.replace("{{ Title }}", title) 
    template_content = template_content.replace("{{ Content }}", html)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = open(dest_path,"w")
    dest_file.write(template_content)
    dest_file.close()
