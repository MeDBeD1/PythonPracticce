import requests
from bs4 import BeautifulSoup
import random as rng

# Организовать словарь русско-английских слов, обеспечивающий перевод русского слова на английский 

rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
root = BeautifulSoup(rs.content, 'html.parser')

dict_dict = {}

for tr in root.select('tr[onmouseover]'):
    td_list = [td.text.strip() for td in tr.select('td')]

    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue

    en = td_list[1]
    ru = td_list[5].split(', ')[0]

    dict_dict[ru] = en

random_key = rng.choice(list(dict_dict.keys()))

print(random_key, "\n", dict_dict[random_key], sep="")