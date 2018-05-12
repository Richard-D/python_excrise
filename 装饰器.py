# 装饰器--装上一个日志
def log(func):
    def wrapper(*args, **kwargs):
        print("call %s(): " %func.__name__)
        return func(*args, **kwargs)
    return wrapper

# @log
def now():
    print("2015-3-25")  # 相当于 now = log(now)

now = log(now)
now()

def log_dev(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("%s %s(): " %(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

now = log_dev('execute')(now)
now()