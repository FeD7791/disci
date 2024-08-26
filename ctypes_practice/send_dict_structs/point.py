import ctypes
import os
 


     
     
path = os.getcwd()

clibrary = ctypes.CDLL(os.path.join(path,'clibrary.so'))



params = {
        #Double Values
        "RadIncrement" : 0. ,
        "BoxSize": 700070 ,
        "MaxRadiusSearch": 40.0,
        "ProxyGridSize": 5.0,
        "FracRadius" : 0.5 ,
        "DeltaThreshold": -0.9,  
        "DeltaSeed": -0.7,
        "OverlapTol":0,
        "Redshift" : 0.99 ,
        "OmegaMatter" : 0.25,
        "OmegaLambda" : 0.75,
        "Hubble" : 0.73,
        "FidOmegaMatter ": 0.2  ,
        "FidOmegaLambda" : 0.8 ,
        "FidHubble" : 0.7, 
        "MinProfileDist ": 0.5,
        "MaxProfileDist" : 3.0,
        "ScalePos":1,
        "ScaleVel" : 1,
        "InnerShellVel": 0.8,
        "OuterShellVel": 1.2,
        #Int Values
        "FormatTracers":0,
        "NumFiles":32,
        "NumRanWalk" : 75 , 
        "OMPcores":8,
        "RSDist" : 0,
        "GDist ": 0,
        "WriteProfiles" : 0 ,
        "NumProfileBins" : 100,   
         
    }

params1 = dict(list(params.items())[0:21])
params2 = dict(list(params.items())[21:29])


p1 = [(key,ctypes.c_double) for key,value in params1.items()] 
p2 = [(key,ctypes.c_int) for key,value in params2.items()]

class InputParams(ctypes.Structure):
    _fields_ = p1 + p2

clibrary.load_input_file.argtypes = [ctypes.POINTER(InputParams)]

p1 = InputParams(**params)

clibrary.load_input_file(p1)