# 57-35 ДЗ

# from abc import ABC, abstractmethod
#
#
# #
# #
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#     @abstractmethod
#     def ploshad(self):
#         pass
#
#     @abstractmethod
#     def print_figure(self):
#         pass
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         self.side = side
#         super().__init__(color)
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def ploshad(self):
#         return self.side ** 2
#
#     def print_info(self):
#         print(f"===Квадрат===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.ploshad()}\n"
#               f"Периметр: {self.perimetr()}")
#         self.print_figure()
#
#     def print_figure(self):
#         print((("*" * self.side) + "\n") * self.side)
#
#
# class Rectangle(Shape):
#     def __init__(self, side1, side2, color):
#         self.side1 = side1
#         self.side2 = side2
#         super().__init__(color)
#
#     def perimetr(self):
#         return 2 * (self.side1 + self.side2)
#
#     def ploshad(self):
#         return self.side1 * self.side2
#
#     def print_info(self):
#         print(f"===Прямоугольник===\nДлинна: {self.side1}\nШирина: {self.side2}\nЦвет: {self.color}\n"
#               f"Площадь: {self.ploshad()}\nПериметр: {self.perimetr()} ")
#         self.print_figure()
#
#     def print_figure(self):
#         print((("*" * self.side2) + "\n") * self.side1)
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, color):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#         super().__init__(color)
#
#     def perimetr(self):
#         return self.side1 + self.side2 + self.side3
#
#     def ploshad(self):
#         return round(0.5 * self.side1 * ((self.side2 ** 2 - (0.5 * self.side1) ** 2) ** 0.5), 2)
#
#     def print_info(self):
#         print(f"===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\n"
#               f"Цвет: {self.color}\nПлощадь: {self.ploshad()}\nПериметр: {self.perimetr()} ")
#         self.print_figure()
#
#     def print_figure(self):
#         for i in range(self.side2):
#             print(" " * (self.side1 // 2 - i) + "*" * i + "*" + "*" * i + "\n", end="")
#
#
# f1 = Square(3, "red")
# f2 = Rectangle(3, 7, "green")
# f3 = Triangle(11, 6, 6, "yellow")
#
# for i in (f1, f2, f3):
#     i.print_info()

# ==============================================================
# 59 урок классы ДОМАШНЕЕ ЗАДАНИЕ

# Создать класс Student,  который будет содержать имя и распечатывать
# информацию, а так же вложенный класс, который будет
# содержать информацию о ноутбуке с техническими характеристиками:
# модель, процессор и память
#
# Roman => HP, i7, 16
# Vladimir => HP, i7, 16

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()  # получим доступ в родительском классе к дочернему
#         # создадим экземпляр класса через инициализатор через переменную
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.rem = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.rem}")
#
#
# st1 = Student("Roman")
# st2 = Student("Vladimir")
#
# st1.show()
# st2.show()

# ================================================================================

# ДОМАШНЕЕ ЗАДАНИЕ ПРО АБСТРАКТНЫЕ МЕТОДЫ! ВАЖНО!
#  Результат может не сойтись но принцип построения верный

# from abc import ABC, abstractmethod
# import math
#
#
# class Root(ABC):
#
#     @abstractmethod
#     def calc(self):
#         pass
#
#
# class Linear(Root):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def calc(self):
#         if self.a == 0 and self.b == 0:
#             print('Бесконечность')
#         elif self.a != 0 and (self.b == 0 or self.a <= self.b):
#             print(f"The root of '3x + 7 = 0' is: {round((-self.b / self.a), 2)}")
#         else:
#             raise TypeError("Корней нет")
#
#
# class Quadratik:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calc(self):
#         d = self.b ** 2 + 4 * self.a * self.c
#         if d > 0:
#             x1 = (self.b + math.sqrt(d) / (2 * self.a))
#             x2 = (self.b - math.sqrt(d) / (2 * self.a))
#             print(f"The roots of '1x^2 - 2x - 3 = 0' are: {x1}, {x2}")
#         elif d == 0:
#             x = self.b / (2 * self.a)
#             print(f"Корень = {x}")
#         else:
#             print("Корней нет")
#
#
# k1 = Linear(3, 7)
# k1.calc()
# k2 = Quadratik(1, 2, 3)
# k2.calc()

# ================================================================================

# урок 61-60-37? дз  Ф у н к т о р (какой то класс который мы можем вызывать как функцию)!!!

# З А Д А Ч А(отредактируй от палева) Создайте функтор для определения порядка сортировки списка
# p, состоящий из обьектов класса Person:
# [('Иванов', 'Игорь', 28),('Петров', 'Степан', 21),('Сидоров', 'Антон', 25),
# ('', '', 11),('', '', 28)]

# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @property # создаем геттер через property
#     def data(self):
#         return self.surname, self.name, self.age
#
#     def __str__(self):
#         return f"{self.surname}, {self.name}, {self.age}"
#
#
# class SortKey:
#     def __init__(self, *args):
#         self.__method = args
#
#     def __call__(self, lst):
#         lst.sort(key=lambda j: [j.__dict__[key] for key in self.__method])
#
#
# p = [Person('Иванов', 'Игорь', 28), Person('Петров', 'Степан', 21), Person('Сидоров', 'Антон', 25),
#      Person('Петров', 'Анатолий', 11),
#      Person('Иванов', 'Иван', 28)]
#
# for i in p:
#     print(i.data)
# print()
#
# s1 = SortKey('surname')
# s1(p)
# for i in p:
#     print(i.data)
# print()
#
# s2 = SortKey('surname', 'name')
# s2(p)
# for i in p:
#     print(i.data)
# ==================================================================================
#  ДОМАШКА ПРОВЕРЬ ВСЕ 62-38 разбор домашки в начале 67-39 урока


# import json
# from random import choice, randint
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = list("abcdefge")  # ['a', 'b', 'b', 'd', 'e', 'f', 'e', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons1.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#
#     with open('persons1.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# # for i in range(5):
# #     write_json(gen_person())
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])
#
# with open('persons1.json', 'r') as f:
#     print(json.load(f))


# ================================================================================



