# Write a Python program to replace all occurrences of space, comma, or dot with a colon
# Phyton programming language. -> Python:programming:language:

import re

string = input()
substitution = re.sub("[ ,.]", "[:]", string)
print(substitution)