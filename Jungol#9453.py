def cal(TF, N):
    if TF == True:
        return str(N) + " + 10 = " + str(N + 10)
    elif TF == False:
        return str(N) + " - 10 = " + str(N - 10)
I = int(input())
print(cal(True, I))
print(cal(False, I))