#Создать класс Животное с атрибутами "имя" и "вид"
#Написать метод который выводит информацию о животном
#в формате "Имя: имя, Вид: вид"

#Для задачи из блока 1 создать две функции, save def u load def,
#которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. 
#Использовать модуль pickle для сериализании и десериализации объектов Python B бинарном формате.

import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"Имя: {self.name}, Вид: {self.species}")

def save(objects, filename):
    with open(filename, 'wb') as f:
        pickle.dump(objects, f)

def load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

animal1 = Animal("Барсик", "Собака")
animal2 = Animal("Мурзик", "Кот")
animal3 = Animal("Пушок", "Хомяк")

animals = [animal1, animal2, animal3]

save(animals, 'animals.pkl')
loaded_animals = load('animals.pkl')

for animal in loaded_animals:
    animal.info()
