# using escape character \
print("1 Hi my name is \"Ankita\"")
print('''2 Hi my name is "Ankita"''')  # this is an alternative to escape character
print("3 Hi my name is \nAnkita ")
print("4 Hi my name is \tAnkita")

print("5 C:\\Users\\Ale\\Python\\Lib")
print(r"6 C:\\Users\\Ale\\Python\\Lib")  # use r or R to ignore escape character

# using slice operator
str1 = "Anonymous"
print(str1[8], " same as " , str1[-1])
print(str1[1:4], " same as ", str1[-8:-5])

# The format method
print("{} in {}".format("Believe", "Yourself"))
print("{1} in {0}".format("yourself", "Believe"))
print("{b} in {y}".format(b="Believe", y="Yourself"))

# Python string functions
firstName = "ANKITA"
lastName = "Ale"

# case related
print(firstName.isupper())
print(lastName.islower())
print(lastName.casefold())
print(firstName.lower())
print(lastName.swapcase())
print(lastName.istitle())

# substring related
str2 = "It never gets easier we just get better"
print(str2.find("we", 0, len(str2)))
print(str2.index("we", 0, len(str2)))
print(str2.partition("we"))

