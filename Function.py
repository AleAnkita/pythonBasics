print("***THE ANONYMOUS FUNCTION : one-line representation of a function***")
sum = lambda num1, num2 : num1+num2
print("Sum = ",sum(20, 40))

# Types of arguments that can be passed in a function
print("Default Arguments - Take default value if no value is provided")
def demo(num1, num2=100):
    return num2 - num1


print(demo(50))
print(demo(40, 60))

print("Keyword Arguments - Mapping the passed values with function arguments using a keyword")
def demo(num1, num2):
    print("Difference = ", num1 - num2)


print(demo(40, 60))
print(demo(num2=20, num1=80))

print("Variable Length Arguments - *args or **kwargs is used as arguments to pass n number of values")
def demo(*mylist):
    newList = []
    for i in mylist:
        newList.append(i + 1)
    return newList


print(demo(12, 24, 36, 48))

print("Required Arguments - Right Order right number of arguments during call")
