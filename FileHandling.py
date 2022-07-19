# two modes of files - Text or Binary
# File Operations - Open,Read,Write,Close

# opening a file - open method
# fileObj = open(<fileName>, <accessmode>, <buffering>)
fileptr = open("demo.txt", "a")
if fileptr:
    print("demo.txt opened successfully")


# Closing a file - close method
# fileObj.close()
try:
    fileptr = open("demo.txt", "a")
finally:
    fileptr.close()


# Writing to a file - a or w access mode write method
fileptr = open("demo.txt", "a")
fileptr1 = open("demo1.txt", "w")

# fileptr.write("Hi this is a demo of write method ")
# fileptr1.write("A file opened in write access mode ")

fileptr.close()
fileptr1.close()


# Reading a file - r and read method
# fileobj.read(<count>) count- number of bytes to be read from the file
fileptr = open("demo.txt", "r")
print("**************************")
content = fileptr.read()  # returns str type
print(content, "\n")

# reading using loop
print("**************************")
fileptr = open("demo.txt", "r")
for i in fileptr:
    print(i)

# reading lines
print("**************************")
fileptr = open("demo.txt", "r")
content1 = fileptr.readline()
print("Line no.1 ", content1)
content2 = fileptr.readline()
print("Line no. 2 ", content2)

fileptr.close()

# tell method to return the position of the pointer byte number
fileptr = open("demo1.txt", "r")
print("The file pointer is at : ", fileptr.tell())

# seek method to modify the position of the pointer - offset, from
fileptr.seek(10)

print("After modifying the position of the pointer :", fileptr.tell())