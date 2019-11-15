def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    count = 0
    for character in str1:
        if character in str2:
            count += 1
            str2 = str2[:str2.index(character)]+str2[str2.index(character)+1:]
    return count == len(str1)
print(is_anagram("silen","listen"))
