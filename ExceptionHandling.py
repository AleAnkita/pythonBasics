# raise is used to create exception for the user when syntactically it is correct
colors = ['Red', 'Blue', 'Black', 'Yellow']
# if len(colors) > 3:
#     raise Exception("Size of the colors is greater than 3")

# assert is used to check valid input or output
def vote(age):
    assert (age > 18), "You are not eligible to vote"
    return "Please Vote"
eligibility = int(input("Enter your age"))
print(vote(eligibility))

# finally - always executed
def reciprocal(num):
    try:
       res = 1/num
    except ZeroDivisionError:
        print("Attempting division by zero")
    else:
        return res
    finally:
        print("Inside finally block")
number = int(input("Enter a number to find reciprocal"))
print("The reciprocal of %d is equals to "%(number), reciprocal(number))

# User - Defined Exception


# List of exception classes
Except_list = ["Exception", "AttributeError", "ZeroDivisionError", "NameError", "IndentationError", "TypeError"]






