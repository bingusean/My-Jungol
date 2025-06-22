import math
from decimal import Decimal, ROUND_HALF_UP
def func(R):
    return "원의 넓이\n버림 : " + str(math.floor(R ** 2 * 3.14)) + "\n올림 : " + str(math.ceil(R ** 2 * 3.14)) + "\n반올림 : " + str(int(float(Decimal(str(R ** 2 * 3.14)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))))
print(func(float(input())))