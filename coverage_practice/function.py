import numpy as np

def calculator(mode, a, b):
    print("calculating")
    c = 7
    if mode=='sum':
        return a+b+c
    elif mode=='abs':
        return np.abs(a-b)