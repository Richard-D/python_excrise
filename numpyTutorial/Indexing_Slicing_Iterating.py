# One-dimensional's operation much ike lists
import numpy as np
a = np.arange(10)
print("Index:", a[2])
print("Slicing",a[1:])
print("Slicing_reserve",a[:-1])
print(a[:6:2])

b = np.array([8,27,64])
print(b)
print(b[:6:2])
a[0:6:2] = 1000
print('[1000,1,1000...] ',a)

# multidimensional arrays
def f(x,y):
    return 10*x+y

c = np.fromfunction(f,(5,4),dtype=int)
print("CCCC",c)
print(c[2,3])
print(c[0:5,1])
print(c[1,0:4])
print("----",c[1,:])

# the dots（...）
d = np.arange(20).reshape(2,2,5)
print(d)
print("1..",d[...,1,2])

# Iterating
for row in d:
    print("Iter:",row)

# Iterating each element
for element in d.flat:
    print(element)


