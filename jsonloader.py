from dataclasses import dataclass
from collections import namedtuple
import json

@dataclass
class User:
    name:str
    age:int
    email:str


with open('data.json', encoding='UTF-8') as jsonfile:
    j = json.load(jsonfile)
    user = User(**j)
    print(user)

    print(json.dumps(user.__dict__))