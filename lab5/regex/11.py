import re

def func(text):
    pattern = "^a*.*(B{5},{6}$)"
    if re.search(pattern, text):
        return "Yes"
        return "No"