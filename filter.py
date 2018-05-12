# filter
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, [' ','A'])))

# 用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        pass
    else:
        break

# 回数
def _series():
    n = 1
    while True:
        yield n
        n = n + 1

def is_palindrom(n):
    return lambda x:str(x)[::-1] == str(x)

def palindrome():
    it = _series()
    while True:
        n = next(it)
        it = filter(is_palindrom(n),it)
        yield n

for n in palindrome():
    if n<999:
        print(n)
    else:
        break