# Write a Python program to convert a given camel case string to snake case
# if our string camel : PythonProgramming, -> snake : python_programming

import re

def camel_to_snake(text):
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
a = input()
print(camel_to_snake(a))
