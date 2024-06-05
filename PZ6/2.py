import random as rng

#Вывести пару соседних чисел из массива которые в сумме ближе всего к число theNum

theNum = rng.randint(0,100)

theList = rng.sample(range(0,100), rng.randint(10,100))
print(theList)

secondList = {}

for i in range(len(theList)-1):
    if i%2 == 0:
        secondList.update(dict.fromkeys([theList[i], theList[i+1]], abs(theList[i] + theList[i+1] - theNum)))

minVal = min(secondList.values())
print(f"{theNum}, {list(filter(lambda x: secondList[x]==minVal, secondList))}")
