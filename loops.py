"""
Task1: Print from 1 - 100
"""
counter = 0
while counter <= 99:
    counter += 1
    print(counter)

"""Given from 100 to 1"""
counter = 100
while counter >= 1:
    counter -= 1
    print(counter)


"""looping from 1 to 100"""
counter = 100
while counter >= 1 and counter <= 100:
    print(101 - counter)
    counter -= 1

"""
Task2: Multiples of 7 between 1 and 1000
"""
counter = 1
while counter <= 1000:
    if counter % 7 == 0:
        print(counter)
    else:
        print("not a multiple")
    counter += 1

"""
Task3:from 1 - 100 print numbers divisible by 3 and 5
then replace with Fizz and Buzz 
respectively 
"""

counter = 1
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter += 1


# FOR loops
names = ["Uche", "Ifihan", "Fuad"]
for i in names:
    print(i)

# Range
for i in range(0, 1001, 5):
    print(i)

"""
Task: 
using FOR loop from 1 - 100 
write a code when divisible by 3 print Fizz
when divisible by 5 print Buzz
when dividible by both 3 and 5 print FizzBuzz
"""
for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# looping through a list
list1 = ["A", "B", "C"]

for num in range(0, 100):
    for item in list1:
        print(num, item)

list2 = ["a", "b"]
for idx, num in enumerate(list2):
    print(idx, num)
