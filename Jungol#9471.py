def func(A, B, C):
    L = [A, B, C]
    return "max: " + str(max(L)) + "\nmin: " + str(min(L))
I, J, K = map(int, input().split())
print(func(I, J, K))