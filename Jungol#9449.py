N, M = list(map(int, input().split()))
CD = {}
for n in range(N):
    I1, I2 = input().split()
    CD.update({I1: I2})
for m in range(M):
    I = input()
    try:
        print(CD[I], end="")
    except KeyError:
        print(I, end="")