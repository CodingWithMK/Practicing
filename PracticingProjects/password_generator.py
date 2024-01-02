import random

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))


password = uppercaseLetter1 + uppercaseLetter2
password = shuffle(password)

print(password)