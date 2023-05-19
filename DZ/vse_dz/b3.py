# НЕОБЯЗАТЕЛЬНАЯ 3 ЗАДАЧА

import random as r

print("Распечатаем матрицу, и одномерный список")
sp = [[r.randint(0, 10) for j in range(6)] for i in range(6)]
one = [r.randint(0, 10) for _ in range(6)]
for i in sp:
    for j in i:
        print(j, end="\t")
    print()
print()
print(one)
print()
sp2 = []
for i in sp:
    if sp.index(i) % 2 == 0:
        i = one
    sp2.append(i)
print("Выведем матрицу с замененными строками")
for i in sp2:
    for j in i:
        print(j, end="\t")
    print()
print()
