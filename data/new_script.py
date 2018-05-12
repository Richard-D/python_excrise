def ynaghui():
    L = []
    L[len(L)-1] = 1
    L[0] = 1
    for n in range(len(L)-1):
        L[n] = L(n-1)[n] + L(n-1)[n-1]
