C0 = C1 = C2 = C3 = C4 = C5 = C6 = C7 = C8 = C9 = 0
for ssm in list(str(int(input()) * int(input()) * int(input()))):
    if ssm == "0": C0 += 1
    if ssm == "1": C1 += 1
    if ssm == "2": C2 += 1
    if ssm == "3": C3 += 1
    if ssm == "4": C4 += 1
    if ssm == "5": C5 += 1
    if ssm == "6": C6 += 1
    if ssm == "7": C7 += 1
    if ssm == "8": C8 += 1
    if ssm == "9": C9 += 1
CS = [C0, C1, C2, C3, C4, C5, C6, C7, C8, C9]
for cs in CS:
    print(cs)
