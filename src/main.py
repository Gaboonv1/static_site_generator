from textnode import TextNode, TextType
from copy_static import sync
from gencontent import generate_pages_recursive

def main():
    sync("static", "public")
    generate_pages_recursive("content","template.html", "public")

main()



if __name__ == "__main__":
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)