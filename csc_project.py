"""SECTION A"""

# Q1 : a program that print my name 100 times
i = 0
for i in range(100):
    i += 1
    print("MAKINDE ISAAC")

# Q2 : a program that print my name horizontally and vertically
i = 0
for i in range(200):
    i += 1
    print("MAKINDE ISAAC", end=" ")

# Q3 : outputs 100 lines with my names on it
for i in range(100):
    i += 1
    print(i, "MAKINDE ISAAC")

# Q4 : a program that computes and print the result (512 - 282) / (47.48 + 5)
x = int(512 - 282)
y = float(47.48 + 5)
print(float(x / y))

# Q5 : print the square of any number
x = int(input("Enter a number: "))
print(x**2)

# Q6 : use sep optional argument to print x,2x,3x ...
x = eval((input("Enter a number: ")))
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep="---")

# Q7: kg to pounds
weight = eval(input("Enter weight in kg : "))
pounds = 2.2 * weight
print(pounds)

"""SECTION B"""
# Q1 converting from lenght to inches
y = eval(input("Enter lenght in'cm':"))
if y < 0:
    print("Invalid Entry ")
else:
    print("The lenght in Inches:", y / 2.54)

# Q2 converting Temperature
x = float(input("Enter a Temperature value:"))
y = input("what the unit? Celsius or Fahrenheit:").lower()
if y == "celsius" or y == "c":
    value = (x * 9 / 5) + 32
    unit = "fahrenheit"
elif y == "fahrenheit" or y == "f":
    value = (x - 32) * 5 / 9
    unit = "celsius"
else:
    print("Invalid unit entered")
print(f"The converted temperature: {value} {unit}")

# Q3 Temperature scale
temp = float(input("Enter a Temperature in celsius:"))
if temp > -273.15:
    print("Invalid temperature. it is below zero")
elif temp == -273.15:
    print("temperature is absolute zero")
elif -273.15 < temp < 0:
    print("temperature is below freezing point")
elif temp == 0:
    print("temperture is at freezing point")
elif 0 < temp < 100:
    print("temperature is in normal range")
elif temp == 100:
    print("temperature is at the boiling point")
else:
    print("tempearture is above the boiling point")
