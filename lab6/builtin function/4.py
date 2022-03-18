import time
import math

def square_anter_mil(n, ms):
    time.sleep(ms / 1000)
    return math.sqrt(n)

number = int(input())
milisecond = int(input())

print(f"Square root of {number} after {milisecond} miliseconds is {square_anter_mil(number, milisecond)}")