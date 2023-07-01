# data types

#  integers
type(5)
print(type(5))
print(int(1.0))
print(int(100))
print(int(10.0))
print(10 // 3)
print(10 % 3)

# variable

x = 5 % 2
print(x)

int_five = int(5.0)
type_of_x = type(int_five)
print(type_of_x)

x, y = 5, 2
print(x, y)

name = input("what your name? ")
print("Hello " + name)

# strings
a = "Hello_class"
b = a[-7:]

str1 = """today is friday,
yes it is """
print(str1)

# write a bio about yourself, check for your name and print the first line of your text

bio = """my name is Isaac,
I\'m learning python programming at Nithub,
python is a beginner friendly programiing language,
i would love to explore the world of technology"""

if "Isaac" in bio:
    print("yes")
firstLine = ""
for i in bio:
    if i != ",":
        firstLine += i
    if i == ",":
        break
print(firstLine)


a = "Hello world"
print(a.replace("H", "J"))

a = "Hello world"
print(a.split("o"))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


name = input("Enter your name:")
age = input("Enter your age:")

a = "Hello world, My name is {name}, I am {age} years old"

print(a.format(age=age, name=name))

name = input("Enter your name:")
age = input("Enter your age:")

a = f"Hello world, My name is {name}, I am {age} years old"

print(a)


name = input("Enter your name:")
age = input("Enter your age:")

a = f"""Hello world, 
My name is {name.title() +' from Nithub'},
I am {age} years old"""

print(a)

# Escape character
# \n
# \t

# concantenation
print("python", 3)
print("python" + "" + "3")
