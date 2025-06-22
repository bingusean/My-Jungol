def func(A, B, C, D, E):
    L = [A, B, C, D, E]
    return max(L) - min(L)
I, J, K, L, M = map(int, input().split())
print(func(I, J, K, L, M))