from string import punctuation
from collections import Counter

def clean_text(text):
    '''
        Lowercase andremovepunctuationfromastring
    '''
    text = text.lower()
    for p in punctuation:
        text = text.replace(p,'')
    text = text.replace('\x00','')
    return text

def load_text(input_file):
    '''
        Load textfromatextfileandreturnasastring.
    '''
    with open(input_file, 'r') as file:
        text = file.read()
    return text

def count_words(input_file):
    '''Count unique words in a string.'''
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)