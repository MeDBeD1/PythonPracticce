#В строках исходного текстового файла все даты представить в виде подстроки, поместить в новый текстовый файл в формате ДД/ММ/ГГГГ

import re

file = open('dates1.txt')
datesString = file.read()
file.close()

datePattern = r"\b(0[1-9]|[12][0-9]|3[01])[./](0[1-9]|1[0-2])[./](\d{4}\b)"
dates = re.findall(datePattern, datesString)

with open("dates.txt", "w") as file:
    for date in dates:
        day, month, year = map(int, date)
        formatted_date = "{:02d}/{:02d}/{:04d}".format(day, month, year)
        file.write(formatted_date + "\n")