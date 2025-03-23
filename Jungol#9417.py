l1 = input().split()
l2 = input().split()
l3 = input().split()
l4 = input().split()

l1 = list(map(int, l1))
l2 = list(map(int, l2))
l3 = list(map(int, l3))
l4 = list(map(int, l4))

i1 = [l1[0] * l3[0], l1[1] * l3[1], l1[2] * l3[2], l1[3] * l3[3]]
i2 = [l2[0] * l4[0], l2[1] * l4[1], l2[2] * l4[2], l2[3] * l4[3]]

print(i1)
print(i2)
