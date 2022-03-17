def swapfirstandlast(target):
    temp = target[0]
    target[0] = target[-1]
    target[-1] = temp
    return target

values = [1,2,3]
print(values)
#print(swapfirstandlast(values))
swapfirstandlast(values)
print(values)