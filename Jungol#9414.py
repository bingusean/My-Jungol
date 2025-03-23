l = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

l[0][0] = 1
l[1][1] = 2
l[2][2] = 3
l[1][3] = 4
l[0][4] = 5

for i in range(3):
    for j in range(5):
        print(l[i][j], end=' ')
    print('')
