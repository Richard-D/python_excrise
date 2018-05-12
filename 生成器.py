g = (x * x for x in range(10))
print(g)

print(next(g))

# 生成器也是课迭代对象
for n in g:
    print(n)

# 斐波那契
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b=b,a+b
        n = n+1
    return 'done'

print("--------------------")
def fib_generator(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'

print(fib_generator(6))

for n in fib_generator(6):
    print(n)

# yield的顺序问题
def odd():
    print("step1")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3

o = odd() #赋值的话，o指向odd()。
next(odd()) #需要注意，这样写的话，只有方法而没有对象
next(o)
next(o)

# 在循环调用generator时，拿不到return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误
g = fib_generator(6)

while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print(e.value)
        break

# 杨辉三角
def triangles():
    L = [1]
    yield L
    n = 2
    while True:
        LL = []
        for j in range(0, n):
            if len(LL) == 0:
                LL.append(1)
            elif len(LL) == n - 1:
                LL.append(1)
            else:
                LL.append(L[j - 1] + L[j])
        L = LL
        n = n + 1
        yield L
print("__________________")
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print("__________________")


str = "adma"
print(str[0].upper())

# 把多维列表展开
def flatten(nested):
    try:
        # 如果是字符串，那么手动抛出TypeError。
        if isinstance( nested, str ):
            raise TypeError
        for sublist in nested:
            # yield flatten(sublist)
            for element in flatten( sublist ):
                # yield element
                print( 'got:', element )
    except TypeError:
        # print('here')
        yield nested


L = ['aaadf', [1, 2, 3], 2, 4, [5, [6, [8, [9]], 'ddf'], 7]]
for num in flatten( L ):
    print( num )



