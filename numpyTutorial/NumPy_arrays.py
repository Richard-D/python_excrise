import numpy as np
one = np.arange(6)
A =np.arange(0,8,2).reshape(2,2)
B = np.arange(4).reshape(2,2)
print(one)
print(A)
print(B)

# basic operation
print("元素乘积：",A*B)
print("matrix product:" ,A.dot(B))

# Such as += and *= ,act in place to modify a existing array
#rather than create a new one
a = np.ones((2,3),dtype=int)
b =np.random.random((2,3))
a = a * 3
print(a)
b = a + b
print(b)

try:
    a+=b
    print(a)
except TypeError as e:
    print("tha a is %s,the b is %s" %(a.dtype,b.dtype))
finally:
    print("end")

# the specifying the axis parameter you can apply an operation
# along the specified axis of an array
d = np.arange(12).reshape(3,4)
print("=====",d)
print("sum of each column ",d.sum(axis=0))
print("sum of each row ",d.sum(axis=1))
print("累加(cumulative)",d.cumsum(axis = 1))

# What is universal function?  such as sin,cos ,and exp，etc
# thess func opreate elementwise on an array
