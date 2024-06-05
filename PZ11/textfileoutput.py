#После строки n из файла вставить случайное слово и создать новый файл с новым текстом

import random as rng
import regex as re

f = open('text18-13.txt', encoding='utf-16')

content = f.read()
print(content, len(content))

newlineIndices = [i.start() for i in re.finditer(r'\n', content)]

randomIndex = rng.choice(newlineIndices)
        
lines = content.split('\n')
        
randomLine = rng.choice(lines[:-1])

words = randomLine.split()
randomWord = rng.choice(words)

newText = content[:randomIndex+1] + randomWord + " " + content[randomIndex+1:]

with open('text18-13-2.txt', 'w', encoding='utf-16') as file:
    file.write(newText)