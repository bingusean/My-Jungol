cycle = 5
numbers = []
temp = []

for i in range(cycle):
    numbers.append(1)
    temp.append(1)
    if i < 2:
        pass
    else:
        for j in range(1, len(numbers) - 1):
            temp[j] = numbers[j - 1] + numbers[j]
    for j in range(len(numbers)):
        numbers[j] = temp[j]
        print(str(numbers[j]) + " ", end="")

    print("")