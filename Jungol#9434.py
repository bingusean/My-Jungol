Input1 = int(input())
Input2 = int(input())
Input3 = int(input())
Input4 = int(input())
Input5 = int(input())
Input6 = int(input())

Input = [Input1, Input2, Input3, Input4, Input5, Input6]

Multiples_of_3 = a = [num for num in Input if num % 3 == 0]
Multiples_of_5 = [num for num in Input if num % 5 == 0]

#합집합
Union = set(list(set(Multiples_of_3) | set(Multiples_of_5)))
#교집합
Intersection = set(list(set(Multiples_of_3) & set(Multiples_of_5)))

print("합집합(union): " + str(Union))
print("교집합(intersection): " + str(Intersection))