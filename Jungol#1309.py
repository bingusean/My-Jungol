I = int(input())
O = []
for i in range(I):
    if i == 0:
        O.append("1! = 1")
    else:
        O.append(str(i + 1) + "! = " + str(i + 1) + " * " + str(i) + "!")
out = 1
for j in range(I):
    out *= j + 1
O.reverse()
for o in O:
    print(o)
print(out)