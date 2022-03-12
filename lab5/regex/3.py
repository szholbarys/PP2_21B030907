# Write a Python program to find sequences of lowercase letters joined with a underscore
# it will be only like this
# abfd_andsk | aaa_bbbb

import re

def matching(text):
    pattern = "^[a-z]+_[a-z]+$" # we use{+} one or more occurences
    if re.search(pattern, text): 
        return "Found matchung!"
    else:
        return ("No matching!") 
a = input()
print(matching(a))           