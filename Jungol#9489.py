def func(dtype, L):
    if dtype == "int":
        return L
    elif dtype == "float":
        res = []
        for x in L:
            res.append(float(x))
        return res
while True:
    J = input()
    if J == "done":
        break
    else :
        I = J.split()
        tpe = I[0]
        del I[0]
        I = list(map(int, I))
        print(func(tpe, I))