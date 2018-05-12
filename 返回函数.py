def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f) # 返回的是函数
print(f()) # 返回的求和结果

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1 = count()
f1[:1]
print(f1)
z = f1[:1]
print(z)


print("*-------------")
f1,f2,f3 = count()
print(f1)
print(f1())


def count_fix():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1,f2,f3 = count_fix()
print(f1)
print(f1())

def createCounter():
    def func():
        n = 1
        while True:
            yield n
            n = n + 1
    num = func()
    def counter():
        return next(num)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# nonolocal，用于操作外层作用域中的对象
def createCounter_two():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

print("-------------------------")

# 利用fs = [],改变[]中的元素
def createCounter_three():
    fs = [0]
    def counter():
        fs[0] = fs[0] + 1
        return fs[0]
    return counter


counterThree = createCounter_three()
print(counterThree(),counterThree())
print("---------------------------")

# 内层函数可以访问外层作用域中的变量
def outside():
    msg = 'outside'
    def inside():
        print(msg)
    inside()
    print(msg)

# 内层函数无法修改外层变量
def outside_():
    msg = 'outside'
    def inside():
        # 无法操作外层变量，这里实际上新建了一个内层局部变量
        msg = 'inside'
        print(msg)
    inside()
    print(msg)

outside_()

# 3. 使用 nonlocal 修改外层变量
def outside_fix():
    msg = 'outside!'
    def inside():
        nonlocal msg
        msg = 'inside!'
        print(msg)
    inside()
    print(msg)

# python的奇怪特性
def outer():
    x = 1
    def inner():
        y = x +1
        print(y)
    inner()
    print(x)

outer()

def outer_fix():
    x = 1
    def inner():
        x = 2
        y = x + 1
        print("y",y)
    inner()
    print(x)

outer_fix()

# 内部修改外部
def outdoor():
    x = 1
    def inner():
        return x + 1
    x = inner()
    print(x)


