# In this Program We will be finding the value of factorial from input using recussive method

n = int(input("Enter a natural number that you want to find a facorial number of: "))

# Function for finding a factorial

def fact(x):
    if x > 1:
        return x*fact(x-1)
    else :
        return 1


if n>=0:
    i = fact(n)
    print("Factorial of",n, "is", i)
else:
    print("Enter a valid natural number")
