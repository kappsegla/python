from operator import attrgetter
import os
import pathlib
import re
import shutil
from datetime import datetime

# path = "files/text.txt"     #Do not use

# path = os.path.join("files","text.txt")  #Pre 3.4

# path = pathlib.Path("files/text.txt")  #Use in 3.4+

# path = pathlib.Path.home()     #User home dir, expanded ~
# filename = input("Enter filename: ")
# path = path / filename

# file = open(path, mode="a", encoding="UTF-8")
# file.write("New info\n")
# file.close()

#remove all files ending with .txt from home folder.
def removetxtfilesfromuserhome():
    path = pathlib.Path.home()
    list = os.listdir(path)
    print(os.getcwd())
    os.chdir(path)      #Change current working directory for this application to user home path
    print(os.getcwd())
    for name in list:
        if name.endswith(".txt"):
            print("Delete " + name)
            os.remove(name)

#find files ending with .log in user home folder.
#if filesize over 100 byte, rename file to .old
#create new .log file with same name but empty
def rotatelogs():
    path = pathlib.Path.home()
    filelist = os.listdir(path)
    for file in filelist:
        if file.endswith(".log") and os.path.getsize(path/file) > 100:
            renamedfile = re.sub("\.log$",".old", file)
            if os.path.exists(path/renamedfile):
                os.remove(path/renamedfile)
            os.rename(path/file, path/renamedfile)
            newfile = open(path/file, mode="w")
            newfile.close()

def backuplogs():
    path = pathlib.Path.home()
    filelist = os.listdir(path)
    for file in filelist:
        if file.endswith(".log") and os.path.getsize(path/file) > 100:
            date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
            newfilename = date + file
            src = path/file
            dest = path/"logs"/newfilename
            if not os.path.exists(path/"logs"):
                os.mkdir(path/"logs")
            #shutil.copy(path/file, path/newfilename)
            if os.name == "posix":
                os.system(f"cp {src} {dest}")   #Unreachable warning in IDE when running on windows, but not an error
            elif os.name == "nt":
                os.system(f"copy {src} {dest}")

class FileInfo:
    def __init__(self, filename, filesize) -> None:
        self.filename = filename
        self.filesize = filesize

    def __str__(self) -> str:
        return f"{self.filename} {self.filesize}"

    def __lt__(self, other):
        return self.filesize < other.filesize

def filesizelist():
    path = pathlib.Path.home()
    filelist = os.listdir(path)
    fileinfolist = []
    for file in filelist:
        if os.path.isfile(path/file):
            fileinfo = FileInfo(file, os.path.getsize(path/file))
            fileinfolist.append(fileinfo)
            
    fileinfolist.sort(key=attrgetter('filesize'), reverse=True)
    #fileinfolist.sort()
    for f in fileinfolist:
        print(f)

filesizelist()

