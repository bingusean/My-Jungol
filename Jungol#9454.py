def func(N,M):
    L = [N, M]
    return "두 수의 합 = " + str(N + M) + "\n두 수의 차 = " + str(max(L) - min(L))
I1, I2 = list(map(int, input().split()))
print(func(I1, I2))

