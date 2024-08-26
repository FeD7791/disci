import ctypes
import os 
import numpy as np

# Load the C library containing the createAndPrintPointArray function
path = os.getcwd()
lib = ctypes.CDLL(os.path.join(path,'c_struct.so'))

# Define the Point and PointArray structures in Python
class Point(ctypes.Structure):
    _fields_ = [("rad", ctypes.c_float ),
                ("x", ctypes.c_float *3),
                ("y", ctypes.c_float *3)]

class PointArray(ctypes.Structure):
    _fields_ = [("points", Point * 1)]




# Set the argument and return types for createAndPrintPointArray
# lib.createAndPrintPointArray.argtypes = []
lib.createAndPrintPointArray.restype = ctypes.POINTER(PointArray)

# Call the createAndPrintPointArray function and receive the pointer
pa = lib.createAndPrintPointArray()

#NUMPY
p_arr = np.ctypeslib.as_array(pa, shape=(7,))
# print(p_arr[0][0][1][0])
print(p_arr)
# Access the points in the PointArray using the pointer
# for i in range(3):
#     print("Point {}: x = {}, y = {}".format(i, pa.contents.points[i].x, pa.contents.points[i].y))

# Deallocate the memory when you're done
free_func = lib.free_memory
free_func.argtypes = [ctypes.POINTER(PointArray)]
free_func(pa)

