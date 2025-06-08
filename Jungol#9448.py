C = int(input())
D = {}
for c in range(C):
    I1, I2 = input().split()
    if I1 == "1":
        if I2 in D:
            D.update({I2: D[I2] + 1})
        else:
            D.update({I2: 1})
    elif I1 == "2":

        if I2 in D:
            print(D[I2])
            del D[I2]
        else:
            print("0")
print(D)