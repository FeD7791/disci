from collections import namedtuple

#Creemos una task nueva con valores por default
Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

task1 = Task('do something', 'okken', True, 21)
print(task1._asdict())