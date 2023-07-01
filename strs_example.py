a = 12
b = 52
c = 365

str1 = "one year has {} months, {} weeks, and {} days"
print(str1.format(a, b, c))

str1 = "one year has {1} months, {0} weeks, and {2} days"
print(str1.format(a, b, c))

str1 = "one year has {index1} months, {index2} weeks, and {index3} days"
print(str1.format(index1=a, index2=b, index3=c))

str1 = f"one year has {a} months, {b} weeks, and {c} days"
print(str1)


task1 = """my name is Adegboyega Samuel,
i'm learning python at nithub 
word of advice for my self
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
Namespaces are one honking great idea -- let's do more of those!"""

print(len(task1))
print("Samuel" in task1)

print(task1.find("Samuel"))
print(task1.index("\n"))

print(task1[:28])

first_line = task1.splitlines()
print(first_line[0])
