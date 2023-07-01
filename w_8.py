"""
List Comprehension
"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 66]

# number divisible by 3
divisible_3 = [i for i in num if i % 3 == 0]
print(divisible_3)

arr = []
for i in num:
    if i % 3 == 0:
        arr.append(i)
print(arr)


names = ["John", "Doe", "Tim"]
ages = [17, 18, 19]

people = [(names, ages) for names, ages in zip(names, ages)]
print(people)


num = [i for i in range(1, 20) if i % 2 == 1]
print(num)

num1 = [i for i in range(1, 1000) if i % 7 == 0]
print(num1)
