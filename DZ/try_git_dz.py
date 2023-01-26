#  ЗАДАЧА 1, 2, 3 ВСЕ ВМЕСТЕ

cort = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(cort)
s = ''
for i in cort:
    if i in s:
        continue
    else:
        print(f'Количество {i} = {cort.count(i)}')
    s += i


# НА ВХОД ФУНКЦИИ ПОСТУПАЕТ СПИСОК ЦЕЛЫХ ЧИСЕЛ.
# В РЕЗУЛЬТАТЕ ВЫПОЛНЕНИЯ ЭТОЙ ФУНКЦИИ БУДЕТ ПОЛУЧЕН КОРТЕЖ УНИКАЛЬНЫХ
# ЭЛЕМЕНТОВ СПИСКА В ОБРАТНОМ ПОРЯДКЕ

# def unics(arr):
#     arr2 = []
#     for i in arr:
#         if i not in arr2:
#             arr2.append(i)
#     return tuple(sorted(arr2, reverse=True))
#
#
# a = [4, 4, 4, 7, 1]
# x = [2, 3, 3, 4, 5, 2]
# print(unics(x))
# print(unics(a))


#  ПОИСК ЗАДАННОГО ЭЛЕМЕНТА В КОРТЕЖЕ
# НЕ ПОНЯЛ КАК ДЕЛАТЬ СДЕЛАЛ ПО СВОЕМУ


# cort = tuple(input("Введите элемент кортежа: ") for _ in range(5))
# print("Исходный кортеж: ", cort)
#
# print('Yes' if input("s = ") in cort else 'No')