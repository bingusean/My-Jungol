def Cal(N):
    L = [I, N]
    return max(L) - min(L)
I = int(input())
J1, J2, J3 = list(map(int, input().split()))
print(Cal(J1))
print(Cal(J2))
print(Cal(J3))