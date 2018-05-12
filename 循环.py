# for X in list/tuple
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# sum = 0
# for x in [1, 2, 3, 4, 5, 6]:
#     sum = sum + x
# print(sum)

# range(num)，可以生成一个整数序列
list(range(5))

for x in range(5):
    print(x)

#while
n =100
sum = 0
while n > 0:
    sum  = sum + n
    print(sum)
    n = n - 1
print(sum)

# break

sum2 = 0
m = 100
print("--------------------")
while m > 0:
    sum2 = sum2 + m
    m = m - 1
    if m == 1:
        print(sum2)
        break;  #结束当前循环
    # sum2 = sum2 + m
    # m = m - 1
print('END')
print(sum2)

# continue
k = 1
while k < 10:
    k = k + 2
    # if k % 2 == 0:
    #     continue
    print(k)




