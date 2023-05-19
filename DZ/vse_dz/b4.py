# НЕОБЯЗАТЕЛЬНАЯ 4 ЗАДАЧА(1 ВАРИАНТ универсальнее, 2-ой по задаче конкретно)

import random as r

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
sp = [[r.randint(0, 10) for j in range(m)] for i in range(n)]
for i in sp:
    for j in i:
        print(j, end="\t")
    print()
print()
for i in range(1, n, 2):
    sp[i], sp[i-1] = sp[i-1], sp[i]
for i in sp:
    for j in i:
        print(j, end="\t")
    print()

# import random as r
#
# sp = [[r.randint(0, 10) for j in range(6)] for i in range(6)]
# for i in sp:
#     for j in i:
#         print(j, end="\t")
#     print()
# print()
# for i in range(1, 6, 2):
#     sp[i], sp[i-1] = sp[i-1], sp[i]
# for i in sp:
#     for j in i:
#         print(j, end="\t")
#     print()



