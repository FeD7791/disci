from wordcountpy import load_text as lt
from wordcountpy import clean_text as ct
from collections import Counter

def count_words(input_file):
    '''Count unique words in a string.'''
    text = lt.load_text(input_file)
    text = ct.clean_text(text)
    words = text.split()
    return Counter(words)
    
    