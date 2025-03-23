l1 = input().split()
l2 = input().split()
l3 = input().split()

l1 = list(map(int, l1))
l2 = list(map(int, l2))
l3 = list(map(int, l3))

c1 = l1[0] + l2[0] + l3[0]
c2 = l1[1] + l2[1] + l3[1]
c3 = l1[2] + l2[2] + l3[2]

print('row_sum :', sum(l1), sum(l2), sum(l3))
print('column_sum :', c1, c2, c3)