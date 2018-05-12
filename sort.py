sorted([36,-21,9,5,-12,])

def by_name(t):
    return t[0]

def by_score(t):
    return t[-1:]

L = [('Bob',75),('Adam',92),('Bart',66)]
L2 = sorted(L,key = by_name)
L3 = sorted(L,key = by_score)
print(L2)
print(L3)