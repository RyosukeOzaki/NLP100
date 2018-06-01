import random

def shuffle1(str):
    str = str.replace(".","")
    str = str.replace(",","")
    str = str.replace(":","")
    str = str.split(" ")
    result = []
    print(str)
    for word in str:
        if len(word)>4:
            print("E")
            chars = list(word[1:-1])
            random.shuffle(chars)
            result.append(word[0]+"".join(chars)+word[-1])

        else:
            result.append(word)
    return " ".join(result)
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = shuffle1(s)
print(result)
