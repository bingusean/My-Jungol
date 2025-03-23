i = input().split()
l = list(map(int, i))
multiples_of_3 = a = [num for num in l if num % 3 == 0]
multiples_of_5 = [num for num in l if num % 5 == 0]
a.extend(multiples_of_5)
print(a)
print("합계: " + str(sum(a))) 