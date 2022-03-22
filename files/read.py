try:
    file = open("text.txt", encoding="UTF-8")
    for line in file:
        print(line)
    file.close()
except:
    print("Couldn't find file")
    exit()

print("More stuff to do")
