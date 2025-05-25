AddInput1, AddInput2 = map(int, input().split())
DiscardInput = int(input())
A = {1, 2, 3, 4, 5}
A.add(AddInput1)
A.add(AddInput2)
print('A = ' + str(A))

A.discard(1)
A.discard(3)

print('A = ' + str(A))

A.discard(DiscardInput)

print('A = ' + str(A))