def func(List):
    print(List)
    for i in List:
        print(i, end=' ')
    print("")
Input = list(map(int, input().split()))
func(Input)