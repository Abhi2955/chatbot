#!/usr/bin/python3
# Writer Abhishek Bishnoi
# module google search
import webbrowser # importing web browser
# defining function to open browser.
def search(word):
    url="http://www.google.com/?#q="
    webbrowser.open_new_tab(url+word)

