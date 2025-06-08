J = input().split()
C = input().split()
for c in C:
    if c in J:
        print(1, end=" ")
    else:
        print(0, end=" ")