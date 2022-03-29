import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name : str
    age : int
    email : str

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
            persons.append( Person(row['name'], row['age'], row['email']))
    
    for x in persons:
        print(x)


readcsvasdictionary()
