# Write a program to check if the given number is palindrome or not.
num = int(input("Enter any Number: "))
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse= (reverse*10)+ remainder
    temp=temp//10

if num==reverse:
    print("Pallindrome")
else:
    print("NP")


# Another Example
text = input("Enter a string: ")

if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
