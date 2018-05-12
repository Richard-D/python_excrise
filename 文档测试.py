# def abs(n):
#     '''
#     Function to get absolute value of number.
#
#     Example:
#
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n>=0 else(-n)


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
      File "D:\python\lib\doctest.py", line 1330, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.fact[2]>", line 1, in <module>
        fact(-1)
      File "E:/python/untitled1/文档测试.py", line 29, in fact
        raise ValueError()
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__=="__main__":
    import doctest
    doctest.testmod()