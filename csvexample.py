import csv
from dataclasses import dataclass
import os
import crypt
import secrets
import string
import re
import getpass
import pwd


@dataclass(frozen=True)
class Person:
    name : str
    age : int
    email : str
    username: str

    def __str__(self) -> str:
       return f"{self.name} is {self.age} years old. Email: {self.email}"


def readcsvaslistwithunpacking():
    persons = []

    with open("data.csv", encoding="UTF-8") as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for name,age,email in csvreader:
            p = Person(name,int(age),email)
            persons.append(p)

    for p in persons:
        print(p)


def readcsvasdictionary():
    persons = []
    with open("data.csv", encoding="UTF-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            persons.append( 
                Person(row['name'],row['age'],row['email'],row['username']))

    return persons

if not getpass.getuser() == "root":
    print("Need root to create users. Start with sudo python...")
    exit()

personlist = readcsvasdictionary()
pat = re.compile("^[a-z][-a-z0-9]*$")

for person in personlist:
    try:
        pwd.getpwnam(person.username)
        print(f"User {person.username} already exist.")
        continue
    except KeyError:
        pass
   
    alphabet = string.ascii_letters + string.digits + "#!&%_;:*?@"
    password = ''.join(secrets.choice(alphabet) for i in range(8))  # for a 8-character password
    print(person.username + ":" + password)  #Should be mailed to user after creating account
    password = crypt.crypt(password, 'sa')
    print(password)
    if re.fullmatch(pat, person.username):
        os.system("useradd -p "+ password +" " + person.username)
    else:
        print(f"{person.username} is not valid")


