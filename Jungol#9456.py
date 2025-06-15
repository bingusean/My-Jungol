def ƒ(x, a, b, c):
    return (a * x**2) + (b * x) + c
A, B, C = list(map(int, input().split()))
print(ƒ(2, A, B, C))
print(ƒ(3, A, B, C))
print(ƒ(5, A, B, C))
