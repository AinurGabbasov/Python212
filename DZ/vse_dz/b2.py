# НЕОБЯЗАТЕЛЬНАЯ 2 ЗАДАЧА
import random as r

sp = [[r.randint(-20, 10) for j in range(4)] for i in range(3)]
otricat = 0
for i in sp:
    for j in i:
        if j < 0:
            otricat += 1
        print(str(j).ljust(4), end=" ")
    print()
print("Количество отрицательных элементов: ", otricat)
