import numpy as np
import os
import ctypes


path = os.getcwd()

clybrary = ctypes.CDLL(os.path.join(path,'carrays.so'))

#Creacion de un arreglo
arreglo = (ctypes.c_int * 10)() #El arreglo es de longitud 10 y todos sus valores estan inicializados a cero

for i in range(len(arreglo)):
    arreglo[i] = i

print(arreglo[1]) # 0 Esto ocurre para todos los elementos

#Generar el output de la funcion de c en python
sum_arr = clybrary.sumarray(arreglo, len(arreglo))
print(sum_arr)


## Esta es la seccion del vector, llamamos al vector


#Para que el codigo funcione el hace esto, retornar el tipo hacia un puntero, si no te tira cualquier cosa
#Para evitar esto una opcion es utilizar los struct de C y retornar eso en lugar de este objeto 
clybrary.inc_array.restype = ctypes.POINTER(ctypes.c_int)

# Input: arreglo y el output proviene de:
out_arr = clybrary.inc_array(arreglo,len(arreglo))




print(out_arr) #<__main__.LP_c_long object at 0x00000288FFF67450> (puntero)
#Para acceder a los contenidos del puntero utilizamos .contents
print(out_arr.contents) #c_long(1)

#Para obtener los resultados reales de la salida del puntero
for i in range(len(arreglo)):
    print(out_arr[i])