persons = []

while True:
    name = input("Skriv ett namn: ")
    if( name == "" ):
        break
    age = int(input("Skriv in ålder: "))
    persons.append((name,age))

for person in persons:
    print(f"Hej {person[0]} du är {person[1]} år")
