# ЗАДАЧА 1

sp = [int(input("-> ")) for i in range(int(input("Введите элемент списка:\nn = ")))]
k = int(input("Введите число:\nch = "))
print("Число присутствует в элементах списка" if k in sp else "Такого числа нет в списке")