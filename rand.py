import numpy as np

print("根据d0-dn创建随机数数组，浮点数，[0,1)，均匀分布",np.random.rand(3,4,5))
print("创建随机数数组，标准正太分布 ",np.random.randn(3,4,5))
print("范围 ",np.random.randint(0,10,(3,4,5)))


np.random.seed(10)
print("seed ",np.random.randn(3,4,5))

np.random.seed(10)
print("样子" ,np.random.randn(3,4,5))

s = np.random.randint(100,200,(2,2))
print(np.random.choice((s,(2,2))))