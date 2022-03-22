from turtle import width


x = 10
y = 10.0
b = True #False

s = "This is text"
l = [1,2,3,4,5]
t = ("Martin", 77) #tuple

names = ["Kalle","Olle"]
points = [100,120]

#Complex datatype
class Student:
    def __init__(self, name, points = 0, active = True):
        self.name = name
        self.points = points
        self.active = active

    def __repr__(self) -> str:
        return f"{self.name} {self.points} {self.active}"

    def __str__(self) -> str:
        return f"{self.name}:{self.points}:{self.active}"

#Create object in memory from class as a template
student1 = Student("Martin", 100)
student2 = Student("Kalle", 200, False)
student4 = Student("Anna", active= False)


print(student4.name)
print(student4.points)
print(student4.active)
print(student4)

student1.name = "Kalle"
student1.points = student1.points + 20
print(student1.name)
print(student1.points)
print(student2.name)

students = [student1, student2]

print(students[0].name)