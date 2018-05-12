class Student(object):
    pass

s= Student
s.name = "M"
print(s.name)

def set_age(self, age):
    self.age = age

# 给实例绑定一个方法
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

# 但是给一个实例绑定的方法对于另一个实例是不起作用的
def set_score(self,score):
    self.score = score


Student.set_score  = set_score
ss = Student()
ss.set_score(100)
print(ss.score)

class Student_slot(object):
    __slots__ = ('name','age') #Y用tuple定义允许允许绑定的属性名称

class GraduateStudent(Student):
    pass

# slot对继承无效
class Person(object):
    __slots__ = ('name','sss')

class man(Person):
    __slots__ =('name','age')

s = man()
s.name = '小明'
s.sss = 99
print(s.name,s.sss)
k = Person()
k.name = "xiaoming"
k.sss = 55
print(k.name,k.sss)

