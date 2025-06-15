def hello():
    print("Hello")
I1, I2 = list(map(int, input().split()))
for i in range(I1):
    hello()
print("")
for i in range(I2):
    hello()