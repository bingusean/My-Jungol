I = input().split()
Is = list(set(I))
D = {}
for i in Is:
    D.update({i:I.count(i)})
# for j in D:
#     print(str(j) + ": " +  str(D[j]))
print("9.5: " + str(D["9.5"]))
print("1.5: " + str(D["1.5"]))
print("5.0: " + str(D["5.0"]))
print("2.5: " + str(D["2.5"]))