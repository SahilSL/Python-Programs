#read
'''
f = open("file.txt", "r")
print(f.read())

g = open("file.txt", "r")
print(g.read(5))

h = open("file.txt", "r")
print(h.readline()) #1st line
print(h.readline()) #2nd line
print(h.readline()) #3rd line
'''

#append : append new text to old file
'''
f = open("file.txt", "a")
f.write("this is append line")
f.close()
f = open("file.txt", "r")
print(f.read())
'''

#write: write new test and delete the old text
'''
f = open("file.txt", "w")
f.write("this is write command")
f.close()
f = open("file.txt", "r")
print(f.read())
'''

#create new file (using x or w):
#f=open("Newfile.txt", "x")

#To remove file
import os
#os.remove("FILE_NAME.txt")
#OR
'''
if os.path.exists("py.txt"):
    os.remove("py.txt")
else:
    print("File doesn't exists")
    '''