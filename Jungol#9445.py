L = []
while True:
    I = input()
    if I != "0":
        L.append(int(I))
    else:
        break
print(set(L))