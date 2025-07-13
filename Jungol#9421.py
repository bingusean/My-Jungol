count = [0] * 7
for _ in range(6):
    num = int(input())
    count[num] += 1
for i in range(1, 7):
    print(f"{i}: {count[i]}")
