l11 = input().split()
l12 = input().split()
l13 = input().split()

l21 = input().split()
l22 = input().split()
l23 = input().split()

l11 = list(map(int, l11))
l12 = list(map(int, l12))
l13 = list(map(int, l13))

l21 = list(map(int, l21))
l22 = list(map(int, l22))
l23 = list(map(int, l23))

print(str(l11[0]+l21[0]), str(l11[1]+l21[1]) + " ")
print(str(l12[0]+l22[0]), str(l12[1]+l22[1]) + " ")
print(str(l13[0]+l23[0]), str(l13[1]+l23[1]) + " ")
