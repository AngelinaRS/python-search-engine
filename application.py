"Search-Engine"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import re

class SearchEngine(object):

    def __init__(self):
        pass

    def reset(self):
        """This cleans the screen"""
        if os.name == "posix": #In linux
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"): #In windows
            os.system("cls")

    def is_space(self, word):
        """This verifies if the word is empty"""
        if word.isspace() == True or word == "":
            return True
        else:
            return False

    def insert_word(self):
        """This saves the word given by the user"""
        self.reset()
        space = True
        while space == True:

            word = raw_input("Insert the word:  ")
            space = self.is_space(word)
            if space == True:
                self.reset()
                #if the word is empty asks again
                print "Insert at least a letter to search\n"
            else:
                return word
        return word

    def first_url(self):
        """This saves the first URL"""
        url1 = raw_input("\nInsert the first URL:  ")
        return url1

    def second_url(self):
        """This saves the second URL"""
        url2 = raw_input("\nInsert the second URL:  ")
        return url2

    def valid_url(self, url):
        """This verifies if the url is valid"""

        try:
            page = urllib2.urlopen(url) #This opens the page
            html = page.read() #This read the page
            return html

        except:
            self.reset()
            return False #If the url is invalid

    def count_page(self, word, url):
        """This counts the times that appear the word"""

        count_url = len(re.findall(word, url))
        return count_url

    def more_repetitions(self, count_url1, count_url2, url1, url2):
        """This show the page that has the more times the word"""

        if count_url1 > count_url2: #if the first page is highest
            self.reset()
            print "\nThis is the page that countains the highest occurrence of the word: ", url1
            print "With %d times" % count_url1

        elif count_url2 > count_url1: #if the second page is highest
            self.reset()
            print "\nThis is the page that countains the highest occurrence of the word: ", url2
            print "With %d times" % count_url2

        #if both pages has the same quantity
        elif count_url1 == count_url2 and count_url1 != 0 and count_url2 != 0:
            self.reset()
            print "\nBoth pages has the same quantity of occurrences"

        elif count_url1 == 0 and count_url2 == 0:
            self.reset()
            print "\nAny page has the word"

    def search(self):
        """This interacts with the user"""
        word = self.insert_word()
        while True:
            url1 = self.first_url() #Insert the first url
            page1 = self.valid_url(url1) #Verifies if is valid
            if page1 == False:
                print "URL invalid\n"
            else:
                while True:
                    url2 = self.second_url() #Insert the second url
                    page2 = self.valid_url(url2) #Verifies if is valid
                    if page2 == False:
                        print "URL invalid\n"
                    else:
                        count_url1 = self.count_page(word, page1) #Counts the first page
                        count_url2 = self.count_page(word, page2) #Counts the second page

                        #Show the url that has the highest ocurrence of the word
                        self.more_repetitions(count_url1, count_url2, url1, url2)
                        self.search_again()

    def minuscule(self, choose_user):
        """This converts the election in minuscule"""
        choose_user = choose_user.lower()
        return choose_user

    def search_again(self):
        """This ask to the user if want to insert another word"""
        while True:
            choose_user = raw_input("\nDo you want to search another word?: y/n ")
            choose_user = self.minuscule(choose_user)

            if choose_user == "y":
                self.search() #Searches again
            elif choose_user == "n":
                self.reset()
                self.menu() #Return to the menu
            else:
                self.reset()
                print "Only can write -y- or -n- "

    def menu(self):
        """This saves the menu"""

        print "1. Search engine"
        print "2. Exit"

        while True:
            choose_user = raw_input("-")

            if choose_user == "1":
                self.search() #Searches the word
                raw_input("Press -Enter-  ")
                self.reset()
                self.menu()

            elif choose_user == "2":
                self.reset()
                sys.exit() #Exit the program

            else:
                self.reset()
                print "//Choose a valid option "
                self.menu()

MAIN = SearchEngine()

#Test Search Engine
if __name__ == '__main__':
    MAIN.menu()
