# 位置函数
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s= s * x
    return s

print(power(2,8))

# 默认参数的坑
def add_end( L = []):
    L.append('END')
    return L

print(add_end([1,2,3,]));
print(add_end([1,2,3,]));
print(add_end())
print(add_end())


def add_end_fix(L = None):
    if  L is None:
        L = []
    L.append('END')
    return L

# 不用可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]))

print('___________________')
# 使用可变参数
def calc_fix(*numbers):
    print(isinstance(numbers,tuple))
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

nums = ((1,2,3))
print(calc_fix(*nums))

# 关键字参数
def person(name, age, **kwargs):
    print('name:', name, 'age:',age,'other:',kwargs)

extra = {'city':'beijing','job':"Engineer"}
person('Jack',24,city = extra['city'],job=extra['job'])
person('John',24,**extra)

# 命名关键字参数
def Person(name,age,*,city,job):
    print(name,age,city,job)

Person('Jack',24,city='Beijing',job='Engineer')


print("______________________________________")
def person_fix(name, age, *args, city, job):
    print(name, age, args, city, job)

print(person_fix('Jack',40,55,65,city='Beijing',job='Engineer'))

# 缺省值
def person_default(name,age,*,city='Beijing', job):
    print(name, age, city, job)
    return

print(person_default('Jack',40,job='Engineer'))

def f1(a, b= 'b',*args,**kwargs):
    print('a =',a,b,args,kwargs)

f1("必选参数", 5,(None,None),city = "关键字参数1",name = "关键字参数2")

f1('a',(None,None),city = "关键字参数1")