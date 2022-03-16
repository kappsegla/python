import mathlib as math

def my_function():
    print("Printed from my function")

def function_with_parameter(name):
    print("Your name is:", name)

def second_function_with_parameters(username, greeting):
    print(greeting,username)

def add(tal1, tal2):
    return tal1 + tal2

my_function()
function_with_parameter("Martin")
second_function_with_parameters("Martin","Hello")

x = math.prod(2,3)
