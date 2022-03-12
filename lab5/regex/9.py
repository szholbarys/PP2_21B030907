# Write a Python program to insert spaces between words starting with capital letter
# if our string : PythonProgrammingLanguage, -> then it will be : Python Programming Language

import re

s = input()
# we need the "join()" function in order to split the string, and it can be split with certain characters
r = re.findall( "[A-Z][a-z]*", s)
print(" ".join((r)))