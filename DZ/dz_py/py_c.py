spisok = list(range(1, 11))
sp = []
for i in spisok:
    sp.append(i ** 2)
print("Список квадратов = ", sp)

# ИЛИ ТАК
# print([i ** 2 for i in range(1, 11)])