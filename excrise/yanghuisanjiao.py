def triangles():
    L = [1]
    while True:
        yield L
        L  = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

def triangle0():
    t = [1,0]
    while True:
        yield t[:-1]
        t = [t[i] + t[i-1] for i in range(len(t))] + [0]

if __name__ == "__main__":
    n = 0
    for t in triangle0( ):
        print( t )
        n = n + 1
        if n == 10:
            break