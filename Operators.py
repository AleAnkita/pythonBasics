# 1. Arithmetic Operators + - / * % // **
var1, var2 = 7, 2
print("// is called floor division and returns integer value", var1//var2)
print("** is called exponent returns power", var1**var2)

# 2. Comparison Operators == != >= <= > <
print("Comparison Operators returns true or false")

# 3. Asssignment Operators = += -= /= *= //= **=
var1, var2 = 7, 2
print("var1 Before", var1)
var1 -= var2
print("var1 After", var1)

# 4. Logical Operators and or not
var1, var2 = 7, 2
print("Is 7 > 2", not var1 > var2)

# 5. Bitwise Operators & | ^ ~ << >>
var1, var2 = 7, 2
print("Binary of 7", bin(var1))
print("Binary of 2", bin(var2))
print("7 | 2 ", var1 | var2)
print("7 ^ 2 ", var1 ^ var2)
print("~ 7", ~ var1)
print("5 << 2", 5 << var2)  # 101 moved left by 2 bits 10100

# 6. Membership Operators in, not in
name = "Shobhan"
oxford = {'a': 'apple', 'b': 'ball', 'd': 'dog'}
print("Does name contains letter b : ", 'b' in name)
print("Does oxford contains c : ", 'c' in oxford)

# 7. Identity Operators is, is not
var1 = 9
var2 = 3*3

print("refer to same object : ", var1 is var2)

# Ternary Operator in Python
x = int(input("Enter a non negative number"))
res = 1 if x==1 else x//2
print("You entered %d This is the result %d" %(x, res))
