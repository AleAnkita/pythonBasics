# import CalculationModule
# from CalculationModule import *

from Modules_directory.CalculationModule import check_even

number = int(input("Enter a number to check if it is even"))

print("The entered number is : ", check_even(number))

# Renaming a module
from Modules_directory import CalculationModule as cal, CalculationModule

print("Enter two numbers to find their sum")
num1 = int(input())
num2 = int(input())

print("The sum of %d and %d is equals to : " % (num1, num2), cal.addition(num1, num2))

# return a sorted list of sub modules
moduleList = dir(CalculationModule)
print("Available sub modules in CalculationModule : ", moduleList)