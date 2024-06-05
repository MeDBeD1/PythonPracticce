import regex as re
import random as rng
import string

#Дана строка – подсчитать кол-во цифр

n = rng.randint(10,20)

theString = ''.join(rng.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=n))

onlyNums = re.findall(r'\d{1}+', theString)

print(f'{theString}\n{len(onlyNums)}')