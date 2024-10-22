import os
#abspath means absolute path gives path from c drive
#relpath means relative path, gives path from current dir
def filepath(filename):
    path=os.path.abspath((filename))
    print(path)

filename="FilePath.py"
filepath(filename)