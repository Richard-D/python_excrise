def cons(x,y,m):
    def dispatch():
        if m == 0: return x
        elif m==1: return y
        else: return "error"
    return dispatch


f = cons(1,2,0)
print(f())
