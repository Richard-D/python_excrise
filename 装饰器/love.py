def love(text):
    def xiangqiushuang(func):
        def denghuang(*args, **kwargs):
            print('%s',(func.__name__ +' ' +  text + xiangqiushuang.__name__) + '?')
            return func(*args, **kwargs)
        return denghuang
    return xiangqiushuang

@love("love ")
def youloveher():
    print("yes")

youloveher()