#PUSH :----->>>
Top=-1
l=[]
for i in range(-1,5):
    if Top==4:
        print("Stack is full")
    else:
        t=int(input("Enter number :"))
        l.append(t)
        Top+=1
print(Top)

#POP:----->>>
print("list is ",l)
for i in range(len(l)):
    if Top==-1:
        print("stack is empty")
    else:
        l.pop()
    Top=Top-1