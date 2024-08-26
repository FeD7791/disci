import os
from sys import path
path0 = os.path.realpath('./wordcountpy/src')
path.append(path0)
from wordcountpy import count_words as cw

print(cw.count_words('zen.txt'))