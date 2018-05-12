import numpy as np

a = np.arange(100).reshape(5,10,2)
np.save("b.npy", a)

print(np.load("b.npy"))