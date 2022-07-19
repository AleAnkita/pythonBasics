# Set Operations
set1 = {"Anji", "Anki", "Barkha", "Komu", "Mansi"}
set2 = {"Anki", "Astha", "Nanne", "Shikhe", "Akshima", "Sakshi", "Jassi", "Kirat"}
print("The Union : ", set1|set2)
print("The Union : ", set1.union(set2))
print("The Intersection : ", set1&set2)
print("The Intersection : ", set1.intersection(set2))
print("The Difference: ", set2 - set1)
print("The Difference: ", set2.difference(set1))
print("The Symmetric difference: ", set1.symmetric_difference(set2))

print("****************************************************************")

# Frozen Sets - Immutable add/update/remove/discard etc. cannot be performed
Fruits = frozenset(('Appple', 'Mango', 'Banana', 'Grapes'))
# this will throw an error
# Fruits.add('Pineapple')

# the use of frozenset comes in storing keys of a dictionary
Dictionary = {1: 'Biology', 2: 'Mathematics', 3: 'Physics' }
frozenKeys = frozenset(Dictionary)
print("set of Keys: ", frozenKeys)
Dictionary[4] = 'Chemistry'
print(Dictionary)
frozenKeys = frozenset(Dictionary)
print("set of Keys: ", frozenKeys)
