l = [[1, 6, 11, 16], [2, 7, 12, 17], [3, 8, 13, 18], [4, 9, 14, 19], [5, 10, 15, 20]]

for i in range(len(l[0])):
    for j in range(len(l)):
        if j == 0:
            print(str(l[j][i]).rjust(2), end=' ')
        else:
            print(str(l[j][i]).rjust(4), end=' ')
    print()