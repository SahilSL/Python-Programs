#WAP to find a fibonacci of a number.
num = int(input("Enter any number: "))
factorial =1
if num<0:
    print("Please enter positive number")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial= factorial*i
    print(factorial)