import numpy as np
def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])
    c = a ** 2 + b ** 2
    print("a的rank: " , a.ndim)
    print("a的尺度: ",a.shape)
    print("a的size:",a.size)
    print("a的元素类型:",a.dtype)
    print("a的每个元素大小:",a.itemsize)
    print("c的type:",c.dtype)
    return c

print(npSum())

## 创建ndaary
n = np.array([[1,2],(2,4),[0,0]])
print("n的rank: ", n.ndim)
print("n的尺度: ", n.shape)
print("n的size:", n.size)
print("n的元素类型:", n.dtype)
print("n的每个元素大小:", n.itemsize)
print("n的type:", n.dtype)

## 使用Numpy中的函数创建ndarray数组，如：arange,ones,zeros等等
print("下面是np里面的方法：")
print("类似range()函数，返回ndarray类型，元素0-n-1：", np.arange(9))
print("根据shape生成一个全1数组：",np.ones((2,3,4),int)) #默认浮点数
print("生成一个全0数组：",np.zeros((2,2),int))
print("生成一个数组，每个元素值都是val:",np.full((2,2),4))
print("创建一个初等矩阵：", np.eye(5))
print("根据数组a的形状城市全0全1全val数组",np.ones_like(n))
print("根据起止数据等间距地填充数据，形成数组：", np.linspace(1,10,4,endpoint=False))
print("合并数组", np.concatenate((n,n)))

# 数组的变换
print("下面是数组的变换:")
s = np.zeros((2,3,4))
m = s.reshape((3,8))
print("返回一个shape形状的数组:",m)
m.resize((2,3,4))
print("修改原数组:",m)
print("返回折叠后的一维数组，原数组不变",s.flatten()) #只能降一维？

# ndarry数组的类型转换
print("ndarry数组的类型转换",s.astype(np.int)) #拷贝

print("向列表转换:" ,n.tolist())

# 对数组的索引和切片
k = np.array([9,8,7,6,5,4,3,2,1])
print(k[2])
print(k[1:4:2])

kk = np.arange(24).reshape((2,3,4))
print(kk[1,2,3])
print(kk[0,1,2])
print(kk[-1,-1,-1])
print("多维数组的切片 ",kk[:,:,::2])

# ndarry运算
# 数组于一个标量的运算作用于数组的每一个元素
print("KK/KK的平均值 ",kk/kk.mean())
print("绝对值 ",np.abs(kk))
print("平凡根 ",np.sqrt(kk))

## 一元运算于二元运算
print("下面是一些运算")
aa= np.eye(5)
bb= np.eye(5)
print(aa)
print(bb)
print(aa==bb)