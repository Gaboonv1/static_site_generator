from textnode import TextNode, TextType
from copy_static import sync
from gencontent import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else: 
        basepath = "/"     

    sync("static", "public")
    generate_pages_recursive("content","template.html", "public", basepath)

main()



if __name__ == "__main__":
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)