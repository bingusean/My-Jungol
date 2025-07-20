N = int(input())
P = []
for n in range(N):
    try:
        P.append(P[-2] + P[-1])
    except IndexError:
        P.append(1)
print(P[-1])