# Types of data types in Python
# Numbers, Sequence, Boolean, Set, Dictionary

# The Numbers type
a, b, c = 2, 3.44, 5 + 9j
print("a=", a, "type of a", type(a))
print("b=", b, "type of b", type(b))
print("c=", c, "type of c", type(c))

# The Sequence Type
print("***************STRING*****************************")
# Strings
msg = "Hi Ankita"
print("msg=", msg, "type of a", type(msg))
print(msg * 3)
print(msg + msg)

# this is a multiline string
msgMulti = '''Hi I am Ankita
learning Python'''
print(msgMulti)

print("*****************LIST*******************************")
# List - diff data type, Mutable
itemList = ["this", 2, "that", 1]
print("itemList", itemList, "type of a", type(itemList))
print(itemList + itemList)
print(itemList * 3)
print(itemList[2:])
print(itemList[0:2])
itemList[2] = "there"
print("After replacing the value in List : ", itemList)
# To find the size of list
print("The number of items in my list is : ", len(itemList))

print("*******************TUPLE*******************************")
# Tuple - diff data type, immutable
itemTuple = ("Here", 7, "There", 4)
print("itemTuple", itemTuple, "type of a", type(itemTuple))
print(itemTuple + itemTuple)
print(itemTuple * 3)
print(itemTuple[2:])
print(itemTuple[0:2])
# itemTuple[2] = "there"
# this will throw error
# print("After replacing the value in Tuple : ", itemTuple)

print("***********************DICTIONARY*****************************")
# Dictionary - Unordered,Mutable, no support for + & *, keys can be any primitive type while values can be any object
itemDict = {1: "Ankita", 2: "Barkha", 'thirdName': "Komal", 'RollNo': [1, 2, 3, 4]}
print("itemDict", itemDict, "type of a", type(itemDict))
print("Items are accessed using key as dictionary is unordered :", itemDict['thirdName'])
print("List of keys: ", itemDict.keys())
print("List of values: ", itemDict.values())

print(itemDict['thirdName'])
itemDict['thirdName'] = "Mansi"
print(itemDict['thirdName'])

print("*********************BOOLEAN*******************************")
# Boolean - True and False
if 5 > 1:
    print("Given condition is : ", True)
else:
    print("Given condition is : ", False)
# Boolean also provides bool method to check truthfulness
# false values are " ", 0, { }, and [ ].
print(bool(0))

print("*********************SET*******************************")
# Set - Unordered, Mutable
Fruits = {'Apple', 'Banana', 'Orange', 'Grapes'}
print("Fruits", Fruits, "type of a", type(Fruits))

vegetables = set()
vegetables.add('Cabbage')
vegetables.update(['Carrot', 'Cucumber', 'Onion'])
print("vegetables : ", vegetables)
vegetables.remove('Carrot')  # discard() is an alternative
print("vegetables : ", vegetables)

print("****************THE END*********************")
