"Search-Engine"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def reset():
    """This cleans the screen"""
    if os.name == "posix": #In linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def insert_word():
    reset()
    word = raw_input("Insert the word:  ")
    return word

def first_URL():
    reset()
    url1 = raw_input("Insert the first URL:  ")
    return url1

def second_url():
    url2 = raw_input("Insert the second URL:  ")
    return url2