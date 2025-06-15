def check(mf, ol):
    ol = int(ol)
    if mf == "M" or mf == 'm':
        if ol > 19:
            return "MAN"
        else:
            return "BOY"
    if mf == "F" or mf == 'f':
        if ol > 19:
            return "WOMAN"
        else:
            return "GIRL"
m, o = input().split()
print(check(m, o))