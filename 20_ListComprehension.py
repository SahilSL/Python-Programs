fruit=["apple", "orange", "Kiwi", "mango"]
newfruit=[]
for i in fruit:
    if "a" in i:
        newfruit.append(i)
print(newfruit)

fruit=["apple", "orange", "Kiwi", "mango"]
newfruit=[x for x in fruit if "i" in x]
print(newfruit)

fruit=["apple", "orange", "Kiwi", "mango"]
newfruit=[x for x in fruit if x!="apple"]
print(newfruit)

fruit=["apple", "orange", "Kiwi", "mango"]
newfruit=[x.upper() for x in fruit]
print(newfruit)