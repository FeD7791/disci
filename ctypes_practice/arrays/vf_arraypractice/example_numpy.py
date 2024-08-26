import numpy as np
import ctypes

c_float_p = ctypes.POINTER(ctypes.c_float)
data = np.array([[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]])
data = data.astype(np.float32)
data_p = data.ctypes.data_as(c_float_p)

print(ctypes.sizeof(data_p))
