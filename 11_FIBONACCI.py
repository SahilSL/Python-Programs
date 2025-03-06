#Write a program to find a fibonacci of a number.
def fibonacci(n):
    if n<=0:
        return "Enter positive number"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        a,b=0,1
        for i in range(2,n):
            a,b=b,a+b
        return b

num= int(input("Enter any number: "))
print(fibonacci(num))


Another EX

num = int(input("Enter the number of terms: "))  
a, b = 0, 1  # First two terms

for n in range(num):
    print(a)
    a, b = b, a + b  # Update values
