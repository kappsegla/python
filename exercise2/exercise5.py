def sum_of_numbers_in_string(string:str):
    sum = 0
    for i in string:
        if i.isdigit():
            sum += int(i)
    return sum


text = "a1b23c"
print( sum_of_numbers_in_string(text))