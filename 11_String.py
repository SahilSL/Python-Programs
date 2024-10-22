a=b=c="Sahil"
 
multiline='''this
 is 
 multi
 line
 string'''
print(multiline)

# Access
x="hjvfcahsvhc"
print(x[5]) # indexing start from 0

for i in x:
    print(i)
    
print(len(x)) # length of str 

str="Hello, this is sahil    "
print("sahil"in str) # return true because it is present in the string
print("Nagpur" in str) # return false because it is not present in the string

#slicing
print(str[2:5]) # start from w and ends at n-1 ie.4
print(str[:5]) # till 5th index
print(str[2:]) #start from 2nd index to end of str
print(str[-5:-2])

print(str.upper())
print(str.lower())

print(str.strip()) #remove extra wide spaces which is present t end of str

print(str.replace('H','Y'))

print(str.split(' ,'))

#string concatenation
a="Hola"
b="folks"
print(a+" "+b)