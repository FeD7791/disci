#Este es el test
from sys import path
import os 
funciones_path = os.path.realpath('..')
path.append(funciones_path)
from functions import function1 as f1

def test_answer():
    assert f1.func(3) == 5
