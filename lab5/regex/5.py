# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# ajdgnjgkndjkgnfdjgnjb | adddddffffb 
# starting with letter a and ending with letter b

import re

def matching(text):
    pattern = "^a.*b$" # we use {.} any characters and {*} zero or more occurences
    if re.search(pattern, text):
        return "Found a matching!"
    else:
        return "Not matching!"
a = input()
print(matching(a))        
