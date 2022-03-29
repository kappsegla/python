def frange(start, stop, step):
    if step == 0:
        raise ValueError
    while( start < stop):
        yield start
        start = start + step


for x in frange(0.5, 5.5, 0.5):
 print(x)

