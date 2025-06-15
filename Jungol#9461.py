I = 0
J = 0
def process():
    global I, J
    if I > J:
        I = I // 2
        J = J * 2
    else:
        J = J // 2
        I = I * 2
I, J = map(int, input().split())
process()
print(I, J)
