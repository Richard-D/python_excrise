import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score =score

s = Student("Bob",20,88)

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

print(json.dumps(s,default=student2dict))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str =  '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# f = open("zz.txt","w")
# d = dict(name = "Bob",age = 20, score = 88)
# json.dump(d,f)

# with open("zz.txt","r") as ff:
#     zz = ff.read()
#     print(json.loads(zz))

with open("zz.txt","r") as ff:
    print(json.load(ff))

