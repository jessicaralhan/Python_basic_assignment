#0 1 1 2 3 5 8 13 21 34 55
#0 1 2 3 4 5 6 7  8  9  10
#Fibonacci Series

#Assignment 2: Write a python program to print out the Fibonacci series of digits between 1 to 100. 
# Try to achieve this using all the types of loop available in python.



def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else: 
        return fibonacci (n-2) + fibonacci(n-1) 
    
print( fibonacci(30) )

for n in range(1,35):
    print(fibonacci(n))