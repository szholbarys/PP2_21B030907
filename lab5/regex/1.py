# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s
# its like
# abbbbb | a | abb | ab

import re

def matching(text):
    pattern = "^a(b*)$" # we use {^} starts with, {*} zero or more occurences and {$} ends with
    if re.search(pattern, text):
        return "Found a matching!"
    else:
        return "Not matching!"         
a = input()
print(matching(a))