'''
a==b
a!=b
a<b
a>b
a<=b
a>=b
'''

a=33
b=55
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
    
    
a=55
b=55
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are same or equal")
else:
    print("b is greater than a")
    
    
a=22
b=200
c=500
if a>b and c<a: #meet both condition
    print(a)
else:
    print(b)
    
a=22
b=200
c=500
if a>b or c<a: #check only one condition
    print(a)
else:
    print(b)