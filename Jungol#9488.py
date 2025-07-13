def func(l):
    res = []
    for x in l:
        res.append(len(x))
    return res
L = input().split()
print(func(L))