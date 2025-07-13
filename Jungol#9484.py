L = list(map(int, input().split()))
answer = []
for i in range(len(L)):
    if L[i] == max(L):
        answer.append(i)
for i in answer:
    print(i, end=" ")