# ЗАДАЧА 4
import random as r

sp = [[r.randint(0, 4) for j in range(3)] for i in range(4)]
mult = 1
for i in sp:
    for j in i:
        if j > 0:
            mult *= j
        print(j, end="\t")
    print()
print("Произведение ненулевых элементов: ", mult)
