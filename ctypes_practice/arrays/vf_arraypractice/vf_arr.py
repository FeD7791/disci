import os
import ctypes
import numpy as np

path = os.getcwd()

#Importo la libreria de C
clibrary = ctypes.CDLL(os.path.join(path,'clibrary.so'))

#Esta seria una forma clasica
c_double_p = ctypes.POINTER(ctypes.c_double) 
data = np.array([1.1,1.3,1.5], dtype=np.float64)

clibrary.printer_arr.argtypes = [c_double_p, ctypes.c_int]

data_p = data.ctypes.data_as(c_double_p) 

clibrary.printer_arr(data_p,len(data))

#Ahora voy a recibir un arreglo desde mi libreria
clibrary.return_array.restype = ctypes.POINTER(ctypes.c_float)
returned_array = clibrary.return_array()
# print(returned_array.contents)
# for i in range(10):
#     print(returned_array[i])

python_arr = np.ctypeslib.as_array(returned_array,shape=(10,))
print(python_arr)
# print(returned_array)
# clibrary.free_memory(returned_array)
# print(returned_array)