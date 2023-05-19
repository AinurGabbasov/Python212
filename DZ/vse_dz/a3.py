# ЗАДАЧА 3
import random as r

sp = [r.randint(0, 100) for i in range(10)]
print(sp)
sp.sort(reverse=True)
print(sp)
