import numpy as np
from decimal import *
a = np.arange(15).reshape(3, 5)

print(a)
print("axes(dimentsion) of a : " , np.ndim(a))
print("axes(dimentsion) of a : " , a.ndim)
print("shape : expected : 5, 3" , a.shape)
print("size : expected : 15", a.size)
print("dtype : expected : int64 : ", a.dtype)
print("dtimezie : expected : 8 : ", a.itemsize)
print("nparray.data : expeced : buffer location " , a.data)
print("nparray.data : expected : a location ", memoryview(a));

def axes(a):
    return np.ndim(a)


def avg(a):
    return np.average(a)

def deviation(a):
    min = avg(a)
    print("xi - min")
    return np.array([xi-min for xi in a])