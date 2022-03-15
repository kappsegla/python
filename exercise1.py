import getpass
import random
#1
name = input("Enter your name: ")
print("Hej",name)

#2
tal1 = int(input("Tal1: "))
tal2 = int(input("Tal2: "))
print("Summa:",tal1+tal2)
print("Produkt:",tal1*tal2)

#3 From python 3 this will work as div by 2.0 For integer division use //
print("Medelvärde: ", (tal1 + tal2) / 2)

#4
tal = int(input("Enter a number: "))
if tal < 100:
    print("Less than 100")
elif tal > 100:
    print("Greater than 100")
else:
    print("Equals 100")

#5
for x in range(1,17):
    print(x, end=" ")

#6
ord1 = ""
while True:
    ord2 = input("Enter text: ")
    if( not ord2 or ord2 == "."):
        break
    ord1 = ord1 + " " + ord2
print(ord1)

#7
secretPassword = "abc123"
enteredPassword = getpass.getpass()
if( secretPassword == enteredPassword):
    print("Authenticated")
else:
    print("Wrong password")

#8
secretNumber = random.randint(1,100)
guesses = 0
while True:
    guess = int(input("Make a guess:"))
    guesses += 1
    if guess == secretNumber:
        print("You found it in", guesses, "guesses")
        break
    elif guess < secretNumber:
        print("Too low")
    else:
        print("Too high")
