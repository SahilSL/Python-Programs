#Write a program to find a minimum of two numbers.
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(maximum(a, b))


#Write a program to find a minimum of three numbers.
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
smallest = 0
if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c
print(smallest, "is the smallest of three numbers.")
