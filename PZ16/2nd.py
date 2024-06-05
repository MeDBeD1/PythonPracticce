#Создать базовый класс "Человек" со свойствами "Имя", "Возраст" и "Пол".
#От этого класса унаследовать классы "Мужчина" и "Женщина"
#Добавить свойства связанные с соц положением 

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Human):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age, "мужчина")
        self.job_title = job_title
        self.salary = salary

class Woman(Human):
    def __init__(self, name, age, marital_status, children):
        super().__init__(name, age, "женщина")
        self.marital_status = marital_status
        self.children = children

man = Man("Петя", 30, "Программист", 80000)
woman = Woman("Маша", 28, "Замужем", 2)

print(man.name)
print(man.salary)
print(woman.name)  
print(woman.children) 
