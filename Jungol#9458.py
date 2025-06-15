def check(N):
    if N > 0:
        return "positive"
    elif N < 0:
        return "negative"
    elif N == 0:
        return "zero"
I = int(input())
print(check(I))