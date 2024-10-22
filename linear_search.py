pos=-1
list=[76,48,36,99,17,23,63]
ele=int(input("Enter number that you want to search : "))
def linear_search(list,ele):
    for i in range(len(list)):
        if list[i]==ele:
            gobals()['pos']=i
            return True
        return False
    
if linear_search(list,ele):
    print("\n number found at location ",pos)
else:
    print("\n Number not found")