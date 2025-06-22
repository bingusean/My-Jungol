from math import *
from decimal import Decimal, ROUND_HALF_UP

def func(A, B, C):
    L = [A, B, C]
    return str(ceil(max(L))) + " " + str(floor(min(L))) + " " + str(int(float(Decimal(str(sorted(L)[1])).quantize(Decimal('1'), rounding=ROUND_HALF_UP))))

I1, I2, I3 = map(float, input().split())
print(func(I1, I2, I3))