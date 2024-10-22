# Write a program to find if the given number is prime or not.

num= int(input("Enter any number: "))
flag = False
if num>1:
    for i in range(2, num):
        if (num % i)==0:
            flag = True
            break

if flag:
    print(f"{num} is not prime Number")
else:
    print(f"{num} is Prime Number")