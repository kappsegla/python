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
    name = "Martin"
    points = 100

#Create object in memory from class as a template
student1 = Student()
student2 = Student()

print(student1.name)
print(student1.points)
student1.name = "Kalle"
student1.points = student1.points + 20
print(student1.name)
print(student1.points)
print(student2.name)

students = [student1, student2]

print(students[0].name)