def keepsome(list, keepfunc):
    templist = []
    for item in list:
        if keepfunc(item):
            templist.append(item)
    return templist

def lessthan5(i):
    return i < 5

def greaterthan3(i):
    return i > 3

someitems = [1,4,10,3]
#keptitems = keepsome(someitems, greaterthan3)
keptitems = keepsome(someitems, lambda i : i < 5 )
print(keptitems)


keptitems = keepsome(someitems, lambda i : i == 4 )
print(keptitems)


# def printgreeting(x):
#     print(x("Hello"))


# printgreeting( lambda input : input.lower() )

