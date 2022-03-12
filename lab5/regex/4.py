# Write a Python program to find the sequences of one upper case letter followed by lower case letters
# its like this
# AaaAAA | Faaaa 

import re

def matching(text):
    pattern = "[A-Z]+[a-z]+$"
    if re.search(pattern, text):
        return "Found a matcing!"
    else: 
        return "Not matching!"    
a = input()
print(matching(a))        