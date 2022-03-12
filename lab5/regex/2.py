# Write a Python program that matches a string that has an 'a' followed by two to three 'b'
# its like
# abb | abbb

import re

def matching(text):
    pattern = "ab{2,3}"
    if re.search(pattern , text):
        return "Found a matching!"
    else:
        return "Not matching!"
a = input()
print(matching(a))            