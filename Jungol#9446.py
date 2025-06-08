T = set(input().split())
G = set(input().split())
TG = T & G
for t in TG:
    print(t, end=' ')