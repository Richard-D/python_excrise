import numpy as np
# ix使得不同维度的向量可以被计算
a = np.array([1,1,1,1])
b = np.array([1,1,1])
c = np.array([1,1,1,1,1])

# 计算 a+b*c
ax,bx,cx = np.ix_(a,b,c)
print(ax.shape,bx.shape,cx.shape)
print((bx*cx).shape)
print(ax+bx*cx,(ax+bx*cx).shape)

def ufunc_reduce(ufct,*vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r,v)
    return r

f = ufunc_reduce(np.add,a,b,c)
print("F\n",f )