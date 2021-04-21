def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
  
a,b=list(map(int,input("Enter two number (a,b): ").split(",")))
print ("The gcd of {0} and {1} is : ".format(a,b),end="") 
print (computeGCD(a,b)) 
