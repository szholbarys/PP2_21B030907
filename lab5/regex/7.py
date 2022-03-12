import re

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
s = input()
print(snake_to_camel(s))