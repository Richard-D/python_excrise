import matplotlib.pyplot as plt
# plt.plot([3,1,4,5,2])
# plt.ylabel("Grade")
# plt.savefig('test',dpi = 600)
# plt.show()

import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)
plt.subplot(2,1,1)
plt.plot(a,f(a))

plt.subplot(212)
plt.plot(a,np.cos(2*np.pi*a),"r--")
plt.show()
plt.plot(a,a*2,"ro--",a,a*5,"g*--")
plt.show()