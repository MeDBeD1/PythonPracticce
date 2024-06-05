#Вывести список со всеми согласными буквами из данного списка

import regex as re

theList = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

consonantsList = []
for word in theList:
    consonantsList.extend(re.findall(r'[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ]', word))

consonantsList = [i.upper() for i in consonantsList]

print("Список согласных букв из заданных слов:", consonantsList)