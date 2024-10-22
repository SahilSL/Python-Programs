tuple=("car","bike","ship")
myit = iter(tuple)
print(next(myit))
print(next(myit))
print(next(myit))
#OR
for x in tuple:
    print(x)

str="apple"
myit = iter(str)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#print(next(myit)) #stop iteration message

#by functions

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass = MyNumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))