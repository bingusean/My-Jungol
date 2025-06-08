C = int(input())
D = {}
for i in range(C):
    I1, I2 = input().split()
    D.update({I1 : I2})
IC = input()
print(D[IC])