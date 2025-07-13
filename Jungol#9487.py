from decimal import Decimal, ROUND_HALF_UP
def rounding(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)
def check(ls):
    count = 0
    for l in ls:
        if l < rounding(l):
            count += 1
    return count
L = list(map(float, input().split()))
print(check(L))