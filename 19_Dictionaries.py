#key-value pair
#changable
#unordered
#not allow duplicate value
# key must be unique

dic={
    "name": "Sahil",
    "age": 21,
    "RollNo":57,
    "favgame":["GTA5","BGMI","UNO"]
}
print(dic)
print(len(dic))

#print particular key value
x=dic["favgame"]
print(x)

dic["name"]="Sahil Lokhande"
print(dic)

dic.update({"name":"undefined"})
print(dic)

dic.pop("favgame")
print(dic)

car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
print(car.get("model"))