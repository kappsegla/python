def sum(tal1,tal2):
    return tal1 + tal2

def prod(tal1,tal2):
    return tal1 * tal2

def max(numbers):
    currentmax = 0
    for x in numbers:
        if( currentmax < x):
            currentmax = x
    return currentmax

    
print(max([1,2,3]))
print(max([3,4,3]))
print(max([10,2,3,20]))