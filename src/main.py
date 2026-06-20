from textnode import TextNode, TextType
from copy_static import sync
<<<<<<< HEAD
from gencontent import generate_page
=======
from gencontent import extract_title, generate_page
>>>>>>> e5a6b741a9e0b071b2c68446570695801dbc36bb

def main():
    sync("static", "public")
    generate_page("content/index.md","template.html", "public/index.html")

main()



if __name__ == "__main__":
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)