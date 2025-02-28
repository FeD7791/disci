from . import function
import numpy as np

def test_calculator():

    a = 3 ; b=2
    suma = function.calculator(mode='sum',a=a,b=b)
    abs = function.calculator(mode='abs', a=a,b=b)
    assert suma == 12
    assert abs == np.abs(a-b)