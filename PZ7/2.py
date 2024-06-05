import random as rng

#Дана строка предложение на русском языке, вывести наибольшее слово

def generateString(length):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя      '
    return ''.join(rng.choice(letters) for _ in range(length))

def sortHelper(theKey):
    return len(theKey)

theString = generateString(rng.randint(10,100))

print(theString)

print(f'{sorted(theString.split(), key=sortHelper)[-1]}')