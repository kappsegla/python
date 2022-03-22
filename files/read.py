try:
    file = open("text.txt", encoding="UTF-8")
    for line in file:
        print(line)
    file.close()
except PermissionError as p:
    print("Wrong permissions")
    exit()
except FileNotFoundError as f:
    print("Couldn't find file")
    exit()
except:
    print("All other errors")

print("More stuff to do")
