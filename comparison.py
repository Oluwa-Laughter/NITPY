# Comparison Operator
print(4 == 5)
print("a" == 65)  # based of ASCII
print("1" >= 1)
print(1 <= 1)
print(0.1 + 0.2)

student_score = 78
grade = 70
num = [70, 78, 34]
num1 = [50]
num2 = 50
print("The results of comparison Operator of student's score and grade are:")
print("Greater than:", student_score > grade)
print("Less than:", student_score < grade)
print("Equal to:", student_score == grade)
print("is operator:", student_score is grade)
print("is not operator:", student_score is not grade)
print("not in:", student_score not in num)

print(student_score >= grade)

print(num1 is num2)

num1.extend([1, 2, 3])
print(num1)

# how to print a memory of address in python
print(id(num1))
