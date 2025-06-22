def func(A, B):
    L = [A, B]
    return max(L) ** 2 - min(L) ** 2
I, J = map(int, input().split())
print(func(I, J))