# data structure

# LIST

list_1 = ["a", "b", "c", "d", "e", "f", "g"]
list_2 = ["boy", 4.8, True, "boy"]
print(list_2)
print(list_2[-3])

print(list_1[0::2])
print(list_1[0:-1:2])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[::-2])

list_1 = ["a", "b", "c", "d", "e", "f", "g"]
print("a" in list_1)
list_1[4:] = 1, 2, 3
print(list_1)

list_1[::2] = 1, 2, 3, 4
print(list_1)

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2[::2] = None, None, None, None, None
print(list_2)

list_2[::2] = [None] * 5
print(list_2)

list_1 = ["a", "b", "c", "d", "e", "f", "g"]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TUPLE

tuple1 = ("apple", "banana", "cherry")

print(tuple1)
print(len(tuple1))

# Dictionary

students = {
    "fuad": ["Fuad", "Adio", "Male"],
    "john": ["John", "Doe"],
    "mary": ["Mary", "doe", "Female"],
    "Chris": [234, "odd", 3.8],
    "total_number": 3,
}

print(students["fuad"])
print(students.get("mary"))
print(students.get("goat", None))
print(students["fuad"][2])
print("mary" in students)

students["john"][1] = 23
print(students["john"])


students["total_number"] = 4
print(students["total_number"])

students.update({"total_number": 4})
print(students["total_number"])

students["Laughter"] = ["abc", "dre", 234]
print(students)

students.update({"Laughter": ["abc", "dre", 23]})
print(students)

print(students.setdefault("Laughter1", "Lucky"))


# SET
