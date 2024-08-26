def load_text(input_file):
    '''
        Load textfromatextfileandreturnasastring.
    '''
    with open(input_file, 'r') as file:
        text = file.read()
    return text