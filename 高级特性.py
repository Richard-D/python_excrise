import random


def trim(s):
    if s == '':
        return s
    if s[0] == ' ':
        s = trim(s[1:])
        print(s)
    if s[-1:] == " ":
        s = trim(s[:-1])
        print(s)
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


st = list(range(9))
print(st[1:])
print(st[0])
print(st[-1]) # 8是-1
print(st[:-1]) #但是这样的话就是从s[-2]开始算
print(st[-2:-1])

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y,y,x)

for x in {'1':'10','2':'20'}.values():
    print(x)

for x in {'1':'10','2':'20'}.items():
    print(x)


print("------------------------------------")

print()
ss = list(range(9))
def findMinAndMax(ss):
    if len(ss) == 0:
        return (None,None)
    if len(ss) == 1:
        return (ss[0],ss[0])
    max = ss[0]
    min = ss[0]
    for i in ss:
        if ss[i]> max:
            max = ss[i]
        if ss[i] < min:
            min = ss[i]
    return (max,min);

print(ss)
print(findMinAndMax(ss))


print('**************')
for i in [(1,2)]:
    print(i)
    print(i[0])

for i in {'0':0,"1":1,"2":2}.items():
    print(i)