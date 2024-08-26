import numpy as np







def writter(val):
    alpha = []
    for i in np.arange(0,20):
        a = i + 2
        e = a*np.linspace(1,10,12)
    alpha.append(np.sum(e))
    return val*np.array(alpha)

for i in range(3):
    k = writter(i)