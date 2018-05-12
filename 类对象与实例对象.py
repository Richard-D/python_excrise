class Student(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# 类属性与实例属性
class attr(object):
    name = "name"

a = attr()
print(a.name)
print(attr.name)
a.name = "another_name"
print(a.name) # 实例属性比类属性优先级高
print(attr.name)