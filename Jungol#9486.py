def func(lis, k):
    smu = sum(lis)
    L = [k, smu]
    return max(L) - min(L)
S = list(map(int, input().split()))
K = int(input())
print(func(S, K))