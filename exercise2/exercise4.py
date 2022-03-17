def balanced(s1,s2):
    chardict = {}
    for character in s2:
       chardict[character] = chardict.get(character, 0) + 1
    
    for x in s1:
       chardict[x] = chardict.get(x, 0) - 1
       if chardict.get(x) < 0:
           return False
    return True

print( balanced("artt", "artgallery"))
print( balanced("artgall", "artgallery"))
print( balanced("övning", "artgallery"))