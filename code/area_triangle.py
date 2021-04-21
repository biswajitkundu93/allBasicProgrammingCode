from math import sqrt


a,b,c=list(map(float,input("Enter three side of a triangle(a,b,c) : ").split(",")))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)