def isisogram(word:str)->bool:
    clean_word = word.lower()
    letter_list = []

    for letter in clean_word:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True


print(isisogram("isogram"))
print(isisogram("isograms"))
print(isisogram("isogram2--!!"))
print(isisogram("Aisogram"))