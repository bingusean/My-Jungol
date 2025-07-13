N = int(input()) + 1
A, B = list(map(int, input().split()))
E = list(range(N))
if A == 0 and B == 0:
    pass
else:
    E[A], E[B] = E[B], E[A]
for i in E:
    print(i, end=" ")