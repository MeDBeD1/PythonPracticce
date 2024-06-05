import random as rng

#Сдвинуть массив влево на число Num с заменой правой части нулями

def shiftLeft(lst, num):
    for _ in range(num):
        lst.pop(0)
        lst.append(0) 
    return lst

newLst = rng.sample(range(1,100), rng.randint(10,100))

Num = rng.randint(0,len(newLst)-1)

print(f"{newLst}, {Num} \n{shiftLeft(newLst,Num)}")