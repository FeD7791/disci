from string import punctuation
def clean_text(text):
    '''
        Lowercase andremovepunctuationfromastring
    '''
    text = text.lower()
    for p in punctuation:
        text = text.replace(p,'')
    text = text.replace('\x00','')
    return text