def cipher(map_from,map_to,code):
    key_code = {}
    decoded = ''
    for index in range(len(map_from)):
        key_code[str(map_from[index])] = str(map_to[index])
    for c in code:
        decoded += key_code[c]
    return (key_code,decoded)
print(cipher("abcd", "dcba", "dab"))
