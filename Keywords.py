# Keywords have unique purpose and meanings
import keyword

print("The list of keywords in this version is: ")
kwList = keyword.kwlist
print(kwList)
print("The total number of keywords present is: ", len(kwList))

print("********************VALUE KEYWORDS = True False None**************************")
# True keyword is equals to '1' and False keyword is equals to '0'
print(True == 3)
print(False == 0)
print(True + True + True)

print("********************OPERATOR KEYWORDS = and or not in is**************************")
# and or will return the component not always True/False
print(3 and 0)
print(3 or 0)
print(not 5)
print("in operator : ")
# in is to check if an element exists in a container
Mylist = [1, 2, 3]
print(1 in Mylist)
print(5 in Mylist)
print("is operator also checks if two arguments relate to unique object: ")
print((9 + 5) is (7 * 2))
print({} is {})
print('' is '')

print("********************ITERATION KEYWORDS = for while break continue**************************")
for i in range(1, 11):
    if i == 7:
        print("skipped for i = 7")
        continue
    else:
        print(i * 3, end=' ')
j = 1
while j < 10:
    print(j + 5, end=' ')
    if j == 8:
        print("stopped at j = 8")
        break
    j = j + 1
print("********************pass return del KEYWORDS**************************")


# pass used to create an empty class/function that might need to be used later
def demo():
    pass

# return is used to return a value from a function otherwise the function returns None keyword
def return_func():
    var = 13
    return var
print("Using return keyword : ", return_func())

# del is used to delete elements from a list and also to delete reference to an object
var1 = var2 = 5
del var1
print(var2)
# print(var1)
print("********************EXCEPTION HANDLING KEYWORDS = try except finally raise assert**************************")
var1 = 4
var2 = 0
try:
    res = var1 / var2
    print("On dividing", var1, "by", var2, "gives", res)
except ZeroDivisionError:
    print("Caught an exception")
finally:
    print(" Finally will be executed no matter what")
# check if var2 is equals to 0
assert var2 != 0, "Divide by 0 error"

