i = input().split()
for j in range(8):
    i.append(str(int(i[-1]) + int(i[-2]))[-1])
for j in range(10):
    print(i[j], end=' ')