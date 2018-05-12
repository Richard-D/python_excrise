L = [1,2,3,4,5]
print(list(map(lambda x:x*x,L)))

def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x:x%2,range(1,20))) # n % 2为真，所以相当于排除掉了n % 2=0的数字
print(L)