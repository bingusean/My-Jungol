Need = set(input().split())
Have = set(input().split())

OnlyNeed = list(Need - Have)
for i in OnlyNeed:
    print(i, end = " ")
print()
