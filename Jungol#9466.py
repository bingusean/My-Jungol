def func(Input):
    L = range(1, Input ** 2 + 1)
    for i in range(Input):
        for j in range(Input):
            print(L[i * Input + j], end=' ')
        print("")
func(int(input()))