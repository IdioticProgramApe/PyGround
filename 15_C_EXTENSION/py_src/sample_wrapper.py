import ctypes
import os
from array import array
from typing import List, Tuple, TypeVar

import numpy as np

pyArray = TypeVar('pyArray', bound=array)
pyList = TypeVar('pyList', List, Tuple)
ndArray = TypeVar('ndArray', bound=np.ndarray)

# try to location the shared library
_file = '..\\sample\\x64\\Release\\sample.dll'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.cdll.LoadLibrary(_path)

# int gcd(int, int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int
    
    
# int in_mandel(double x0, double y0, int n)
in_mandel = _mod.in_mandel
in_mandel.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_int)
in_mandel.restype = ctypes.c_int


# int divide(int a, int b, int *reminder)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x: int, y: int) -> Tuple[int, int]:
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    return quot, rem.value
    
    
# double avg(double *a, int n)
# Define a special type for `double *` argument
class DoubleArrayType:
    def from_param(self, param) -> ctypes.POINTER(ctypes.c_double):
        typename = type(param).__name__
        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)
        elif isinstance(param, ctypes.Array):
            return param
        else:
            raise TypeError("Can't convert %s" % typename)
        
    # cast from array.array objects
    # documentation: https://docs.python.org/3.7/library/array.html
    def from_array(self, param: pyArray):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')
        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))
    
    # cast from lists/tuples
    def from_list(self, param: pyList):
        val = ((ctypes.c_double) * len(param))(*param)
        return val
    
    from_tuple = from_list
    
    # cast from numpy.ndarray
    def from_ndarray(self, param: ndArray):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

DoubleArray = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double

def avg(values):
    return _avg(values, len(values))


# struct Point { ... }
class Point(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_double),
        ('y', ctypes.c_double)
    ]
    
# double distance(Point *p1, Point *p2)
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double
