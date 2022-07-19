import re

# list of metacharacters
meta_char = [".", "^", "$", "*", "+", "?", "{ }", "[ ]", "|", "( )" ]

# match method
msg = "It never gets easier you just get better"
res = re.match(r'g*',msg,re.t)
if res:
    print("found match = ", res.group())

# search method returns first occurrence of the pattern otherwise null

# findall method look for "all" appearances of a pattern
