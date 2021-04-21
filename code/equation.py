from cmath import sqrt


a,b,c=list(map(float,input("Enter a,b,c of equation (a,b,c) : ").split(",")))

# Solve the quadratic equation ax**2 + bx + c = 0

d = (b**2) - (4*a*c)

alpha = (-b-sqrt(d))/(2*a)
beta = (-b+sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(alpha,beta))
