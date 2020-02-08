import numpy as np
from decimal import *
a = np.arange(15).reshape(5, 3)
print(a)

print("axes(dimentsion) of a : " , np.ndim(a))
print("axes(dimentsion) of a : " , a.ndim)


print("shape : expected : 5, 3" , a.shape)

print("size : expected : 15", a.size)

print("dtype : expected : int64 : ", a.dtype)

print("dtimezie : expected : 8 : ", a.itemsize)

print("nparray.data : expeced : buffer location " , a.data)
print("nparray.data : expected : a location ", memoryview(a));
