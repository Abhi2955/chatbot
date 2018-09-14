#!/usr/bin/python3
#Writer: ABHISHEK BISHNOI
# this module is used for search on wikipedia
import wikipedia
import webbrowser

# this functionreturns result of wikipidea.
def wiki(str):
    try:
        result = wikipedia.summary(str, sentences=2)
        url = "http://en.wikipedia.org/w/index.php?title="
        #webbrowser.open_new_tab(url+str)
        return result
    
    except wikipedia.exceptions.PageError:
        url1 = "http://www.google.com/?#q="
        webbrowser.open_new_tab(url1+str)
        return "I did not find any information regarding that query, here the related search results"