def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


def palindrome(text:str)-> bool:
    return text == text[::-1]


def symmetrical(text:str)->bool:
    middle = int(len(text)/2)
    firsthalf=text[:middle]
    secondhalf=text[middle:]
    return firsthalf == secondhalf


text = input("Input: ")
if symmetrical(text):
    print(f"The entered string is symmetrical")
else:
    print(f"The entered string is not symmetrical")

if palindrome(text):
    print(f"The entered string is palindrome")
else:
    print(f"The entered string is not palindrome")
