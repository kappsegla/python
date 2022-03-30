listitems = [1,2,3,4,5]

result = filter(lambda x: x >= 3, listitems)

for item in result:
    print(item)

strings = ["Hej", "" , "abc", "123", "Kalmar"]
result = filter(lambda s: s != "", strings)

for s in result:
    print(s)

result = map(lambda s: len(s), strings)

for s in result:
    print(s)


    