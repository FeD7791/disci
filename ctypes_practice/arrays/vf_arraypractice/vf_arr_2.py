#Arrays con numpy ctypeslib
import os
import ctypes
import numpy as np

path = os.getcwd()

#Importo la libreria de C
clibrary = ctypes.CDLL(os.path.join(path,'clibrary.so'))

#Creacion del puntero del arreglo que hace referencia a un arreglo con las siguientes caracteristicas:
# - El tipo es np.float64
# - La dimension (opcional) es 1
# - flags: 
#       -C_CONTIGUOUS: The data is in a single, C-style contiguous segment (numpy.ndarray.flags)
#       -ALIGNED: The data and all elements are aligned appropriately for the hardware (no es necesario aca)
# Observacion np.foat64 <----> double en C
# Observacion 2: ctypes.c_float <----> float en C
arr_point = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags=['C_CONTIGUOUS'])

#Mi arreglo en Numpy
np_arr = np.array([1.1,1.7,8.2], dtype=np.float64)

#De momento llamare a la funcion printer, inputs: arr , len(arr)
clibrary.printer_arr.argtypes = [arr_point, ctypes.c_int]

clibrary.printer_arr(np_arr,len(np_arr))