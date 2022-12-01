# Remove duplicate items from the given list
from typing import List
list1 = [1, 2, 2 , 3 , 55 , 98, 65, 65, 13, 29]
list2 =[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("original list ", list1)
print("After removing duplicate items ", list2)

# Find the common element in the given lists
list3 = [1, 2, 3, 4, 5, 6]
list4 = [7, 8, 9, 2, 10]
for i in list3:
    if i in list4:
        print("The common element is ", i)

 
""" Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """
