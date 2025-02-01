from enum import Enum
from textnode import *

def main():
    #print("hello world")
    thing = TextNode("This is a text node", TextType("bold"), "http://www.website.org")
    print(thing)


main()