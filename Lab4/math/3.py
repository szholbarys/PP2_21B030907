#calculate the area of regular polygon
# from math import tan, pi
# side = int(input())
# lside = int(input())

# area = int(side * (lside ** 2)/(4 * tan(pi/side)))
# print(area)
from math import tan, radians

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

p = n*l
a = l/(2*tan(radians(180/n)))

print(f'The area of the polygeon is: {int(p*a/2)}')