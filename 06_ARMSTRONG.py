# Write a program to check if the given number is Armstrong or not.
num=int(input("Enter any number: "))
temp = num
sum=0

while temp>0:
    digit =temp%10
    sum+= digit**3
    temp =temp//10

if num==sum:
    print("Armstrong")
else:
    print("Not Armstrong")