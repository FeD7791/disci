import os
import ctypes

path = os.getcwd() #get current working directory path
clibrary = ctypes.CDLL(os.path.join(path,'clybrary.so'))

#Esta es la funcion para reservar memoria
alloc_func = clibrary.alloc_memory #Primero defino la funcion desde la libreria de C
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)  # restype indica a python el tipo del resultado

#Esta es la funcion para liberar memoria
free_func = clibrary.free_memory
free_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

#Escribo el puntero
c_str_pointer = alloc_func()

#Tratamos de imprimir el valor que viene en el puntero
cstring = ctypes.c_char_p.from_buffer(c_str_pointer) #from_buffer retorna un objeto ctypes

#Veamos que sucede
print(c_str_pointer) #Memory Allocation<__main__.LP_c_char_p object at 0x00000149A339B150>
print(cstring) # c_char_p(2119031223712)
print(cstring.value) #b'Hello world'

#Liberamos la memoria
free_func(c_str_pointer)

#Si vuelvo a llamar a cstring:
print(cstring.value) #No escribe nada porque no hay nada 