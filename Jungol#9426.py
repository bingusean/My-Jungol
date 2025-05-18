inp = int(input())
pascal = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

epas = pascal[0:inp]
epas.reverse()
for dsd in epas:
    for dsdd in dsd:
        print(dsdd, end=" ")
    print("")
