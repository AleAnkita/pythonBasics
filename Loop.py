# The for Loop
# Program to calculate the cubes of 5 numbers
sum = 0
for i in range(5):
    num = int(input("Enter a number"))
    sum += num ** 3
print("The sum of cubes of 5 numbers entered by user i s: ", sum)

# The nested for loop
import random

myList = []
for i in range(1, 11):
    myList.append(random.randint(0, 20))
print("This is the List: ", myList)
for j in range(1, 11):
    for k in myList:
        if j == k:
            print(j, end=' ')
print("*****************************************************")

# The while Loop
# Program to print table of a given number
tab = int(input("Enter a number to print its table"))
i = 1
while i<=10:
    print("%d X %d = %d \n" % (tab, i, tab * i))
    i += 1


