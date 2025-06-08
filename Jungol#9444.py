I = list(map(int, input().split()))
I.remove(I[0])
I.remove(I[-1])
print(tuple(I))