import os
import pathlib

path = "files/text.txt"     #Do not use

path = os.path.join("files","text.txt")  #Pre 3.4

path = pathlib.Path("files/text.txt")  #Use in 3.4+

path = pathlib.Path.home()     #User home dir, expanded ~
filename = input("Enter filename: ")
path = path / filename

file = open(path, mode="a", encoding="UTF-8")
file.write("New info\n")
file.close()

#remove all files ending with .txt from home folder.
path = pathlib.Path.home()
list = os.listdir(path)
print(os.getcwd())
os.chdir(path)      #Change current working directory for this application to user home path
print(os.getcwd())
for name in list:
    if name.endswith(".txt"):
        print("Delete " + name)
        os.remove(name)

