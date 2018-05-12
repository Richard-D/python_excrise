class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__

print(Student("M"))
s = Student("K")
print(s)

## 编程list，tuple那样的iterable
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if  self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# 按下标访问任意一项
def __getitem__(self,n):
    a,b = 1,1
    for x in range(n):
        a,b = b, a+b
    return a

Fib.__getitem__ = __getitem__
m = Fib()
print(m[2])

# 但是list有一个神奇的切片方法，而Fib报错
# print(m[0:5])

def __getitem__(self, n):
    if isinstance(n, int):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        return L

Fib.__getitem__ = __getitem__
z = Fib()
print(z[0:5])

# getattr
class Student(object):
    def __getattr__(self, item):
        if item == 'age':
            return lambda : 25
        raise AttributeError('zz')
sss = Student()
print(sss.age())
#print(sss.abc)  返回None,因为哦我们定义的默认返回就是None

# 链式调用
class Chain(object):
    def __init__(self,path=""):
        self.path = path

    def __str__(self): #Chain(path)
        return self._path

    def __getattr__(self, path):
        return Chain("%s/%s" %(self._path,path))

    __repr__ = __str__

# 直接对实例进行调用
class Student_call(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("My name is %s " %self.name)

s = Student_call("M")
s()
