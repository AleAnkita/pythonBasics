num = int(input("Enter the number of elements you want in the series "))

while num <= 0:
    num = int(input("Please enter a valid number "))
    if num > 0:
        break

myList = [0, 1]
for i in range(2, num):
    myList.append(myList[i-1] + myList[i-2])
print("This is your Fibonacci Series : ", myList)
