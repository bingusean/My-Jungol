def func(lis):
    lis.remove(max(lis))
    return max(lis)
I = list(map(int, input().split()))
print(func(I))