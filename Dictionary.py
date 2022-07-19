# dictionary creation using dict method
Subjects = dict([(1, "Biology"), (5, "History"), (2, "Physics"), (3, "Mathematics"), (4, "Geography") ])

# deleting elements of Dictionary
Subjects.pop(4)
print("Using pop Subjects: ", Subjects)
Subjects.popitem()  # for last item
print("Using popitem Subjects: ", Subjects)
Subjects.clear()
print("Using clear Subjects: ", Subjects)
# del Subjects
# print("Using del Subjects: ", Subjects)

# traversing Dictionary using loops
Subjects = dict([(1, "Biology"), (5, "History"), (2, "Physics"), (3, "Mathematics"), (4, "Geography") ])
for i in Subjects.values():
    print(i, end=" ")
print("\n")
for i in Subjects.items():
    print(i, end = " ")
print("\n")
for i in Subjects:
    print(Subjects[i], end = " ")

# Creating shallow copy of Dictionary
dict1 = {1:"A", 2:"B", 3:"C", 4:"D"}
dict2 = dict1.copy()
print("\n", dict1 == dict2)
print(dict1 is dict2)
print("dict2 = ", dict2)


