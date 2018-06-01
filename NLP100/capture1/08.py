def cipher(str):
    result = []
    for alp in str:
        if alp.islower():
            new_alp = chr(219-ord(alp))
            result.append(new_alp)
        else:
            result.append(alp)
    return "".join(result)

s = "Boron"
result = cipher(s)
print(result)
