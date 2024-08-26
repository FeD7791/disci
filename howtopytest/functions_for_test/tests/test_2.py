import os
from sys import path

class_path = os.path.realpath('..')
path.append(class_path)
from functions import class1 as cl1


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = cl1.Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
    'owner': 'okken',
    'done': True,
    'id': 21}
    assert t_dict == expected