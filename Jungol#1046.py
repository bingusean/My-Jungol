from decimal import Decimal, ROUND_HALF_UP

def round_half_up(value, decimal_places=2):
    # 소수 둘째 자리까지 사사오입 반올림
    quantize_str = '0.' + '0' * (decimal_places - 1) + '1'
    return float(Decimal(str(value)).quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP))
N = int(input())
OC = list(map(int, input().split()))
RESES = []
res = 0
while True:
    if OC == []:
        break
    RESES.append((max(OC) + min(OC)) / 2)
    OC.remove(max(OC))
    try:
        OC.remove(min(OC))
    except ValueError:
        pass
res = max(RESES)
print(round_half_up(res))