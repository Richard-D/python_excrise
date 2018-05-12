class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %s" %(self.name, self.score))

bart = Student("denghuang","97")
print("我们来看看未实例化的信息 ", Student) #一个类
print("我们来看看实例化后的信息 ", bart) #一个对象
lisa = Student("lisa","99")
bart.print_score()
print("我们来看看类中方法的地址:" ,Student("denghuang","97").print_score) ##我想打印出方法的地址

## 访问限制与数据封装
# 外部无法访问的name与score
class Student_fix(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Bad Score")

bart = Student_fix("J",99)
bart.set_score(80)
print(bart.get_name())
print(bart.get_score())
print(bart._Student_fix__name) # 还是可以通过这种方式访问
bart._Student_fix__name = "K"
print(bart._Student_fix__name)
