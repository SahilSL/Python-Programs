#Lambda ----> it is anonymous function
'''
x= lambda a: a+20
print(x(5))
'''
'''
x= lambda a,b: a+b
print(x(5,30))
'''
'''
def f1(n):
    return lambda x: x*n
doun=f1(2)
trip=f1(3)
print(doun(11))
print(trip(11))
'''

#Filter---->
'''
def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True
filtered= filter(prime, range(10))
print("Prime numbers are: ", list(filtered))
'''

#Maps---->
'''
def square(x):
    return x*x

numbers=[1,2,3,4,5]
listsquares= map(square, numbers)
print(listsquares)
print(list(listsquares))
'''

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else: 
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(fun, sequence)
print('The filtered letters are:') 
for s in filtered:
    print(s)