import ctypes
import numpy as np 
import os 

path = os.getcwd()
# clybrary = ctypes.CDLL(os.path.join(path,'arreglos2.so'))
clybrary = ctypes.CDLL(os.path.join(path,'func_arr_c.so'))





# Observacion np.foat64 <----> double en C
# Observacion 2: ctypes.c_float <----> float en C

# #INPUT
# arr_point = np.ctypeslib.ndpointer(np.float64, ndim=1, flags=['C_CONTIGUOUS'])
# array = np.linspace(0,50,50,dtype=np.float64)
# #array = (ctypes.c_int * 10)()

# clybrary.inc_array.argtypes = [arr_point,ctypes.c_int]

# #OUTPUT
# clybrary.inc_array.restype = ctypes.POINTER(ctypes.c_double)

# output = clybrary.inc_array(array,50)
# print(output)

# python_arr = np.ctypeslib.as_array(output,shape=(50,))
# print(python_arr)
# print(output[5])

## OTHER FUNCTION
clybrary.create_arr.restype = ctypes.POINTER(ctypes.c_float)
output2 = clybrary.create_arr()
p_arr = np.ctypeslib.as_array(output2, shape=(50,))
print(p_arr)