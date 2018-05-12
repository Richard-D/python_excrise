# hsplit
import numpy as np
a = np.floor(10*np.random.random((2,12)))
print("a",a)
b = np.hsplit(a,2)
print(b)

c = np.hsplit(a,(3,4))
print(c)

# the view method creates a new array object look like at the
# same data

d = a.view()
assert d is not a

d.base is a
assert d.base is a

# a's shape doesn't change
print("AAA",a)
# c.shape = 3,6

d[0,0:12] = np.arange(12)
print("CCCC",d)
print("aaaa",a)
