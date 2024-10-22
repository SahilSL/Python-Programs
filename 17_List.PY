# can contain string, num, bool, pr mix datatype
#ordered
#can be change
#allow duplication

list=["car",50,True,2.6]
print(list)
print(len(list))
print(type(list))
print(list[2])
print(list[-1])

#slicing
print(list[1:3])
print(list[2:])
print(list[:3]) 

#edit/change
list[0]="Audi"
print(list)

list.insert(4,"jeep")
print(list)

list.insert(1,"LAMBO")
print(list)

list2=[1,2,5,6]
list.append(list2)
print(list)

lsi = ["apple", "banana", "cherry"]
lsi.remove("banana")
print(lsi)