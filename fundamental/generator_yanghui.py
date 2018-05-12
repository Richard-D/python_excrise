def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n + 1
    return "donn"

m = []
for n in fib(6):
    m.append(n)
    print(m)

# 递归
def triangles(n):
    def _triangles(n,result):
        if n == 1:
            return [1]
        else:
            L = [sum(i) for i in zip([0] + result,result + [0])]
        return L

    pre_result = []
    for i in range(n):
        pre_result = _triangles(i + 1, pre_result)
        yield pre_result

for x in triangles(5):
    print(x)


def triangles2(n):
    result = [1]
    for x in range(n):
        yield result
        result = [sum( i ) for i in zip( [0] + result, result + [0] )]

def triangles3():
    L = [1]
    while  True:
        yield L
        L.insert(0,0)
        L.append(0)
        L = [L[i] + L[i+1] for i in range(len(L)-1)]

def triangles4(n):
    count = 0
    t = []
    while True:
        for i in range(len(t) -1):
            t[i] = t[i] + t[i+1]
        t.insert(0,1)
        yield t[:]


print("4",triangles4(5))


l1 = [1]
l2 = []
for i in range(3):
    l1[0] += 1
    print(id(l1))
    l2.append(l1)
print(l2)

for i in triangles2(6):
    print("2",i)