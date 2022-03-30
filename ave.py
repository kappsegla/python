from functools import reduce
from statistics import mean

numbers = [1,2,3,4,5,6,7]

print( sum(numbers) / len(numbers) )
print(mean(numbers))

s = reduce(lambda x,y: x + y, numbers)
print( s / len(numbers))

def biggest(x,y):
    if x > y:
        return x
    else:
        return y

print(max(numbers))
m = reduce(biggest, numbers)
print(m)

def smallest(x,y):
    if x < y:
        return x
    else:
        return y

print(min(numbers))
m = reduce(smallest, numbers)
print(m)

print(len(numbers))
l = reduce(lambda x,y: x + 1, numbers, 0)
print(l)

print( reduce(lambda x,y: x*y, numbers))

