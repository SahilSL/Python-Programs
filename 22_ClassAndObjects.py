'''
class human:
    x=5
h1=human
print(h1.x)
'''

'''
class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
h1=human("sahil",21)
print(h1.name)
print(h1.age)
'''

'''
class human:
    #self is namespace of class and objects in python
    #you can also use any name other than self
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def methods(self):
        print("hi! my name is "+self.name)
    
        
h1=human("sahil",21)
h2=human("rahul",5)

h1.methods()
h2.methods()
'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
'''

'''
class MyClass:
    x = 5 ** 10
 
p1 = MyClass()
print(p1.x)
'''