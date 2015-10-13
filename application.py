"Search-Engine"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import re

def reset():
    """This cleans the screen"""
    if os.name == "posix": #In linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def is_space(word):
    """This verifies if the word is empty"""
    if word.isspace() == True or word == "":
        return True
    else:
        return False

def insert_word():
    """This saves the word given by the user"""
    reset()
    space = True
    while space == True:

        word = raw_input("Insert the word:  ")
        space = is_space(word)
        if space == True:
            reset()
            #if the word is empty asks again
            print "Insert at least a letter to search\n"
        else:
            return word
    return word

def first_url():
    """This saves the first URL"""
    url1 = raw_input("\nInsert the first URL:  ")
    return url1

def second_url():
    """This saves the second URL"""
    url2 = raw_input("\nInsert the second URL:  ")
    return url2

def valid_url(url):
    """This verifies if the url is valid"""

    try:
        page = urllib2.urlopen(url) #This opens the page
        html = page.read() #This read the page
        return html

    except:
        reset()
        return False #If the url is invalid

def count_page(word, url):
    """This counts the times that appear the word"""

    count_url = len(re.findall(word, url))
    return count_url

def more_repetitions(count_url1, count_url2, url1, url2):
    """This show the page that has the more times the word"""

    if count_url1 > count_url2: #if the first page is highest
        reset()
        print "\nThis is the page that countained the highest ocurrence of the word: ", url1
        print "With %d times" % count_url1

    elif count_url2 > count_url1: #if the second page is highest
        reset()
        print "\nThis is the page that countained the highest ocurrence of the word: ", url2
        print "With %d times" % count_url2

    #if both pages has the same quantity
    elif count_url1 == count_url2 and count_url1 != 0 and count_url2 != 0:
        reset()
        print "\nBoth pages has the same quantity of ocurrences"

    elif count_url1 == 0 and count_url2 == 0:
        reset()
        print "\nAny page has the word"

def search():
    """This interacts with the user"""
    word = insert_word()
    while True:
        url1 = first_url() #Insert the first url
        page1 = valid_url(url1) #Verifies if is valid
        if page1 == False:
            print "URL invalid\n"
        else:
            while True:
                url2 = second_url() #Insert the second url
                page2 = valid_url(url2) #Verifies if is valid
                if page2 == False:
                    print "URL invalid\n"
                else:
                    count_url1 = count_page(word, page1) #Counts the first page
                    count_url2 = count_page(word, page2) #Counts the second page

                    #Show the url that has the highest ocurrence of the word
                    more_repetitions(count_url1, count_url2, url1, url2)
                    search_again()

def search_again():
    """This ask to the user if want to insert another word"""
    while True:
        choose_user = raw_input("\nDo you want to search another word?: y/n ")
        if choose_user == "y":
            search() #Searches again
        elif choose_user == "n":
            reset()
            menu() #Return to the menu
        else:
            reset()
            print "Only can write -y- or -n- "

def menu():
    """This saves the menu"""

    print "1. Search engine"
    print "2. Exit"

    while True:
        choose_user = raw_input("-")

        if choose_user == "1":
            search() #Searches the word
            raw_input("Press -Enter-  ")
            reset()
            menu()

        elif choose_user == "2":
            reset()
            sys.exit() #Exit the program

        else:
            reset()
            print "//Choose a valid option "
            menu()

#Test Search Engine
if __name__ == '__main__':
    menu()
