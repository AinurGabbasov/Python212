# 38 УРОК. ЛОКАЛЬНЫЕ ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ В ФУНКЦИЯХ
# ПЛЮС СЛОВАРИ

# НАПИШИТЕ ФУНКЦИЮ КОТОРАЯ ПРИНИМАЕТ ПРОИЗВОЛЬНОЕ КОЛИЧЕСТВО АРГУМЕНТ И ВОЗВРАЩАЕТ
# СЛОВАРЬ В КОТОРОМ КАЖДЫЙ ЭЛЕМЕНТ СПИСКА ЯВЛЯЕТСЯ
# И КЛЮЧОМ И ЗНАЧЕНИЕМ

# def func(*a):
#     return {i: i for i in a}
#
#
# print(func(1, 2, 3, 4))
# print(func("gray", (2, 17), 3.11, -4))


# 1 MIN написать функ, которая принимаем произвольное число чисел,
# вычисл их среднее арифметическое и возвращает те б которые меньше полученного арифметического

# def funcc(*a):
#     sr = sum(a) / len(a)
#     return [i for i in a if i < sr]
#
#
# print(funcc(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(funcc(3, 6, 1, 9, 5))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args):
#     res = []
#     for i in args:
#         res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# МИНУТ 7 точно Создайте функ, которая принимает неогран колво параметров ключ значение
# и обновляет созданный словарь my_dict. он должен обновлятся при каждом ыызове функ

# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
#
# print("my_dict =", my_dict)

# scope - ОБЛАСТЬ ВИДИМОСТИ

# УРОК 39 ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ

# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))

# второй способ задачи выше через глобальную переменную(scip)
# функция ведущая подсчет городов

# def func(city):
#     t = 0
#
#     def vnutr():
#         nonlocal t
#         t += 1
#         print(city, t)
#
#     return vnutr
#
#
# res = func('Москва')
# res()
# res()
#
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()


#  у р о к 40  фильтр мап редук зип декораторы
#
# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# Создать лям выраж для нахожд мин значения между тремя числами 9, 8, 5 3мин

# print((lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))(5, 8, 9))

# map(func, iterable) где func  лучше делать через лямбда выражение! либо инт или стр


# s = ['1', '2', '3']
# print(list(map(int, s)))

# s = [2.4234, 3.2341, 4.8564]
# print(list(map(lambda x: round(x, 2), s)))

# Найти поэлементно сумму двух списков 2MIN

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, iterable)

# 3 MIN
# from random import randint
# b = [randint(0,100) for i in range(10)]
# print(b)
# print(list(filter(lambda x: 10 <= x <= 20, b)))

# 30 sec
# sp = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda x: x % 15 == 0, sp)))


# декораторы одна из полезных тем!!!

#  Создать декоратор, который будет принимать в виде вргумента
#  число, которое будет умножаться на число принимаемое функцией
# def multiply(a):
#     def wrapper(fun):
#         def wrap(b):
#             return a * fun(b)
#
#         return wrap
#
#     return wrapper
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(6))

# ================================================================================

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#     return wrap
# @cnt
# def hello():
#     print("Hello")
#
# @cnt
# def g():
#     print("Hell")
#
# hello()
# hello()
# hello()
# g()
# g()

# ================================================================================

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут ", first, last)
#
# print_full_name("Ирина", "Ветрова")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("Данные: ", args)
#         print("Данные: ", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study)
#
#
# print_full_name("Ирина", "Елена", "Анна", study="Java")
# print_full_name("петя", "вася", "гоша")

# =================================================================================
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(9, 1)

# ==================================================================================

# декоратор с исключением

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z
#
#
# print(type_fn(3, 4, 5))
# print(type_fn(3, 4, 'ewr'))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z
#
#
# print(type_fn(3, 4, 5))


# ПЕРЕВОД В СИСТЕМЫ СЧИСЛЕНИЯ ЧЕРЕЗ ИНТ или через методы
# print(int("100", 2))
# print(int("100", 8))

# print(bin(18)) #  десятичное число переводим в ДВОИЧНОЕ ДАЛЬШЕ ВОСБМИРИЧНОЕ И ШЕСТНА-ОЕ
# print(oct(18))
# print(hex(18))
#
# print(0b10010) # и обратно из двоичной в десятичн
# print(0o22)
# print(0x12)

# Пузырьковая bubble сортировка
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1):
#             if array[i] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10000)]
# print(a)
# bubble(a)
# print(a)


# ПОВТОРИ ДЕКОРАТОР СХЕМУ

# def g(h):
#     def w(*args, **kwargs):
#         print("декорируем функцию с разных сторон")
#         print("декорируем функцию с разных сторон")
#         res = h(*args, **kwargs)
#         print('hoho')
#         print("декорируем функцию с разных сторон")
#         return res
#
#     return w
#
#
# @g
# def hj(ert, tag):
#     print(f'lalala = {ert}, tag = {tag}')
#     return f"<{tag}>{ert}</{tag}>"
#
#
# res = hj("DECORATISHE", 'h1')
# print(res)


# СЛОВАРИ

# print("введите название одного из 4х овощей")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# u = int(input("какой элем удалить? "))
# del d[u]
# print(d)


# ПРЕОБРАЗУЕМ ДВА СЛОВАРЯ В ОДИН

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y # с версии 3.9
# print(z)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)


# ТАК МОЖНО ПЕРЕПИСАТЬ НАЗВАНИЕ КЛЮЧА НА НОВОЕ НАЗВАНИЕ

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# re.sub(pattern, repl, string, max=0)
# Этот метод заменяет все вхождения pattern в string на repl, если не указано на max.
# Он возвращает измененную строку.

# ==================================================================================

# Регулярные выражения 26.01.23 32пара


# import re
#
# # print(dir(re))
#
# s = "Я ищу совпадения в 2023 году. И я их 1234 найду в 2 [сч]ёта."
# # reg = r'[2023]' # в квадратных скобках это поиск одного из символов(можно воспринимать как множество символов)
# # print(re.findall(reg, s)) # возвращает список содержащий все совпадения с заданным шаблоном
#
# # print(re.search(reg, s)) # возвращает данные по соответствию ПЕРВОГО совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# # print(re.match(reg, s)) # поиск по заданому шаблону в начале строки
#
# # print(re.split(reg, s, 1)) # разбили строку по шаблону НА СПИСОК ПОДСТРОК
#
# # print(re.sub(reg, "!", s, 1)) # ЗАМЕНА ШАБЛОНА НА ДРУГОЙ СИМВОЛ, ПОИСК-ЗАМЕНА(1 - ЭТО ТО СКОЛЬКО РАЗ)
#
#
# # =========================================================================
# # reg = r'[1-2][0-9][0-9][0-9]' # так можно найти год
#
# reg = r'[А-яёЁ.\[\]]' # чтоб найти все русские буквы, а еще точка в [] скобках это именно точка!
# print(re.findall(reg, s))

# =======================================================================
#  ЗАДАЧА
# import re
#
# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09"
#
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))
# =====================================================================
#
# import re
#
# s = "Я ищу совпадения в 2023 году. И я соих 1234 найду в 2 счёта. 9812. [Hello]"
#
# # reg = r'\s' # любой пробел
# # reg = r'\S' # все что угодно кроме пробела
# reg = r'со'
# print(re.findall(reg, s))

# class Car:
#
#     def __init__(self, color, consumption, tank_volume, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = tank_volume
#         self.reserve = tank_volume
#         self.mileage = mileage
#         self.engine_on = False
#
#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."
#
#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return "Двигатель остановлен."
#         return "Двигатель уже был остановлен."
#
#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый запас топлива."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."
#
#     def refuel(self):
#         self.reserve = self.tank_volume
#
#     def get_mileage(self):
#         return self.mileage
#
#     def get_reserve(self):
#         return self.reserve
#
#
# car_1 = Car(color="black", consumption=10, tank_volume=55)
# print(car_1.__dict__)

# ========================================================================

# class SomeClass(object):
#     def __init__(self, name):
#         self.name = name
#
#     # def __del__(self):
#     #     print('удаляется объект {} класса SomeClass'.format(self.name))
#
#
# obj = SomeClass("John");
# print(obj.__dict__)

# ==================================================================
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = nums[0]
current_sum = nums[0]

for i in range(1, len(nums)):
    num = nums[i]

    current_sum = max(current_sum + num, num)
    max_sum = max(current_sum, max_sum)
print(max_sum)