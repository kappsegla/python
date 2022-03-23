from colorama import init
from colorama import Fore, Back

string1 = "GAGCCTACTAACGGGAT"
string2 = "CATCGTAATGACGGCCT"

def hammingdistance(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count = count + 1
    return count

def colordiff(a,b):
    colorstring1 = ""
    colorstring2 = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            colorstring1 += Fore.RED + Back.WHITE + a[i]
            colorstring2 += Fore.RED + Back.WHITE + b[i]
        else:
            colorstring1 += Fore.WHITE + Back.BLACK +a[i]
            colorstring2 += Fore.WHITE + Back.BLACK +b[i]

    return (colorstring1, colorstring2)

class color:
    RED = "\033[91m"
    WHITE = "\033[0m"


init()

print("Hamming distance: " + str(hammingdistance(string1, string2)))
if hammingdistance(string1, string2) > 5:
    print("Doesn't look the same at all")
result = colordiff(string1,string2)
print(result[0])
print(result[1])











""" 
for i in range(len(string1)):
    if string1[i] != string2[i]:
        print("\033[94m" + string1[i], end="")
    else:
        print("\033[91m"+string1[i], end="")
    print("\033[0m", end="") """

