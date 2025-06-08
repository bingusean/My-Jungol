C = int(input())
L = []
for c in range(C):
    I1, I2 = input().split()
    L.append(I1)
    L.append(int(I2))
print("[", end="")
for j in range(C):
    print("('" + str(L[2 * j]) + "', ", end="")
    print(str(L[2 * j + 1]) + ")", end="")
    if j != C - 1:
        print(", ", end="")
print("]")