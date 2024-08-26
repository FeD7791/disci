import ctypes

#Para utilizar nuestra funcion tenemos que llamar a nuestro objeto libreria
clibrary = ctypes.CDLL("C:\\Users\\Fede\\Desktop\\ingenieria_software\\miTeoria\\ctypes_practice\\test.so") #Debe tomar el path del archivo C
# clibrary.display()
# clibrary.display2(b"Federico", 32) #Pasamos argumentos a nuestra funcion / Hay que usar la b para pasar strings


# Otra manera de llamar a una funcion de C
func = clibrary.display3
func.argtypes = [ctypes.c_char_p,ctypes.c_int]
func.restype = ctypes.c_char_p

print(func(b"Federico",32))