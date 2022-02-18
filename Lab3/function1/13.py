import random

print("Hello! What is your name?")
s = input()

print()

print(f'Well, {s}, I am thinking of a number between 1 and 20.')
print("Take a guess.")

n = random.randrange(0,20)

x =- 1
cnt=0

while x != n:
    k = int(input())
    print()
    if k < n:
        print('Your guess is too low.')
        print("Take a guess.")
    else:
        print('Your guess is too bigger.')
        print("Take a guess.")
    x = k
    cnt += 1 

print(f'Good job, {s}! You guessed my number in {cnt} guesses!')