A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

Union = A & B
Intersection = A | B
ComplementAB = A - B
ComplementBA = B - A

print("A & B = " + str(Union))
print("A | B = " + str(Intersection))
print("A - B = " + str(ComplementAB))
print("B - A = " + str(ComplementBA))