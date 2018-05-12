f  = abs
def add(x,y,f):
    return f(x) + f(y)
print(add(-5,6,f))

def ff(a,n=2,m=3):
    return a[0] ** n + a[1] ** m

L = []
for i in [(1,2),(3,4)]:
    L.append(i[0])
print(ff(L))

# 使用map计算任意复杂的函数
print(list(map(str,(list(range(0,10))))))

# reduce把一个函数作用在一个序列上
from functools import reduce
def add_r(x,y):
    return x * 10 +y

print(reduce(add_r,[1,3,5,7,9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(char2num('1'))

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def add_rr(x,y):
        return x*10+y
    def char2num_r(s):
        return digits[s]
    return reduce(add_rr, map(char2num_r , s))

print(str2int('13579'))

# lambda函数进一步简化
def str22int(s):
    return reduce(lambda x,y: x * 10+y,map(char2num,s))

alphabet = {"A":"a","B":"b","C":"c","L":"l"}

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    t=name[:1].upper()+name[1:].lower()
    return t

t = map(normalize,L1)
print(next(t))
print(next(t))

def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数
def str2float(s):
    def char2num(s):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7, '8': 8, '9': 9}
        return digits[s]
    def add(x,y):
        return x * 10 + y
    L,R = s.split(".")
    L1 = reduce(add, map(char2num,L))
    return L1 + pow(10,-len(R)) * reduce(add,map(char2num,R))

print(str2float("126.1235"))
