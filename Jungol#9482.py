def func(List):
    List.reverse()
    return List
For = int(input())
L = []
for i in range(For):
    L.append(input())
print(*func(L))
