I = input()
D = {"dog":1, "cat":2, "rabbit":3}
if I in D:
    print(D[I])
else:
    D.update({I : 4})
    print("dic =",D)