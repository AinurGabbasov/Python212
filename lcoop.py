# 10.01.23 OOP тут все понятно свойства методы и метод для отдельного доступа к атрибутам класса
import csv

# class Human:
#     name = "name"
#     biirthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print("Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.biirthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.biirthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name): #  Метод для отдельного доступа к имени
#         self.name = name
#     def get_name(self):
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Лена", "23.11.1989", "23-34-45", "Россия", "Москва", "Сойкина, 5А")
# h1.print_info()
# h1.set_name("Маша")
# h1.print_info()
# print(h1.get_name())


# Инкапсуляция

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # закрытые переменные __x __y
#             self.__y = y
#
#     def set_x(self, x):  # установить
#         self.__x = x
#
#     def get_x(self):  # получить
#         return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y  # возвращение нескольких значений идет в виде кортежа
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.x = 100 + 1
# # p1.y = 'sef'
# # print(p1.x, p1.y)
# p1.set_coords(4.56, 4.234)
# print(p1.get_coords())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 123 # если обратится через системное имя все равнно можно изменить значение переменной!!
# print(p1.__dict__)


# создать класс Rectangle описывающий прямоугольник.
# В классе должны быть все необходимые методы, а так же методы вычисления
# площади, периметра и диагонали и метод который рисует прямоугольник
# from math import sqrt
#
#
# class Rectangle:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_perim(self):
#         return 2 * (self.__x + self.__y)
#
#     def get_gip(self):
#         return sqrt(self.__x ** 2 + self.__y ** 2)
#
#     def print_area(self):
#         print(('*' * self.__y + '\n') * self.__x)
#
#
# r1 = Rectangle(3, 4)
# r1.set_x(3)
# r1.set_y(9)
# print(r1.get_y(), r1.get_x())
# print(r1.get_area())
# print(r1.get_area())
# print(round(r1.get_gip()))
# r1.print_area()
#
# r2 = Rectangle(2, 14)
# r2.print_area()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Сеттер")
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 100.7
# print(p1.coordX)
# print(p1.__dict__)
# del p1.coordX
# print(p1.__dict__)


# Используем пропрти через декоратор, в питоне ооп это часто бывает

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coordX(self):
#         print("Геттер")
#         return self.__x
#     @coordX.setter
#     def coordX(self, x):
#         print("Сеттер")
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#     @coordX.deleter
#     def coordX(self):
#         print("Удаление свойства")
#         del self.__x
#
#
# p1 = Point(5, 10)
# p1.coordX = 100.7
# print(p1.coordX)
# print(p1.__dict__)
# del p1.coordX
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, j):
#         self.__old = j
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 35
# print(p1.name, p1.old)
# p1.old = 39
# del p1.old
# p1.old = 98
# print(p1.__dict__)

# ООП ГЕТЕРЫ СЕТЕРЫ ЗАКРЫТЫЕ ПЕРЕМЕННЫЕ ЗАДАЧА
# Создать класс для преобразования киллограмм в фунты
# 12кг => 26.46 фунтов
# 41 кг => 90.405 фунтов
# Киллограммы задаются только числами!!!
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Киллограммы задаются толкьо числами!")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.to_pounds())
# w.kg = 'десять'


# Создайте класс для подсчета максимума из четырех аргументов(3, 5,7,9),
# минимума из 4ех аргументов, среднеарифмитического из 4ех аргументов,
# факториала аргумента(5). функциональность реализовать в виде статических методов.

# class Nunbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         if b > a and b > c and b > d:
#             return b
#         if c > a and c > b and c > d:
#             return c
#         if d > a and d > b and d > c:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         if b < a and b < c and b < d:
#             return b
#         if c < a and c < b and c < d:
#             return c
#         if d < a and d < b and d < c:
#             return d
#
#     @staticmethod
#     def sred(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fac(a):
#         fa = 1
#         for i in range(1, a + 1):
#             fa *= i
#         return fa
#
#
# print(Nunbers.max(1, 2, 3, 4))
# print(Nunbers.min(1, 2, 3, 4))
# print(Nunbers.sred(1, 2, 3, 4))
# print(Nunbers.fac(4))

# =================================================================================
# новая задачка сделать класс который работает с какой то датой
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# # d = "16.12.2021"
# # day, month, year = map(int, d.split("."))
# # date = Date(day, month, year)
# # d = Date()
# # date = Date.from_string("16.12.2021")
# # print(date.string_to_db())
# # d1 = Date()
# # date = Date.from_string("18.02.2021")
# # print(date.string_to_db())
# dates = [
#     '30.12.2021',
#     '29-12-2013',
#     '01.04.2022'
# ]
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print('Неверный формат даты')

# ======================================================================================

# Урок 54 статические методы, примеры выше тоже оттуда
# Создайте класс для подсчета площади геом-х фигур.
# Класс должен представлять функциональность для подсчета
# площади треугольника по разным формулам, площади прямоугольника,
# квадрата. Методы класса для подсчета площади должны быть реалезованы
# с помощью статических методов/
# НЕ РЕШЕНО

# ===========================================================================

# Урок 55 статические методы, методы класса, наследование
# Создать класс "Account" представляющий собой банковский счет. Класс должен содержать:
# - динамические свойства: фамилия владельца, номер счета, процент начисления, сумма в рублях;
# -статические свойства: курс рубля по отношению к доллару , курс рубля по отноошению к евро;
# - классовые методы: редактировать курс рубля по отнош...

# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname  # фамилия владельца
#         self.num = num  # номер счета
#         self.percent = percent  # процент начисления
#         self.value = value  # сумма в рублях
#         print(f'Счет #{num} принадлежащий {surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # редактирование курса рубля по отношению к доллару
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # редактирование курса рубля по отношению к евро
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):  # Смена владельца счета
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_euro)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def add_percents(self):  # начисление процентов
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # Снятие заданной суммы
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):  # Вывод информации о счете
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# ========================================================================================================

# НАСЛЕДОВАНИЕ\ базовый класс родительский\ дочерний производный класс\

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Prop:
#
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Базовый инициализатор")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# rect = Rect(Point(3, 4), Point(23, 34))
# line.draw_line()
# rect.draw_rect()
# # line.width = 10
# # print(line.width)
# # line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # print(rect.width)


# ===================================================================================

# Наследование. Создание и управление поведением экземпляров класса

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rect(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter  # В сеттерах мы пишем УСЛОВИЯ!
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Значение ширины должно быть больше 0")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Значение высоты должно быть больше 0")
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         # return self.color
#         # return self.width * self.height  # с помощью геттеров
#         # return self.border_new("1px solid gray")
#
#
# rect = Rect(10, 20, "green", "1px solid gray")
# print(rect.area())

# закончили наследование 56урок 39мин:12сек
# ===================================================================================================

# Создать класс "Liquid" (жидкость) со свойствами: название и плотность жидкости, -
# и методами: изменения плотности, вычисления обьема жидкости,
# соответствующего заданной массе,
# вычисление массы жидкости, соответствующему заданному обьему,
# вывод информации о жидкости.

# Создать производный класс "Alcohol"(спирт) с собственным свойством - крепость,
# и методом - изменение крепости

# class Liquid:
#     def __init__(self, name, density):
#         self._name = name  # с одним подчеркиванием как раз используют при наследовании
#         self._density = density  # плотность жидкости
#
#     def edit_density(self, val):
#         self._density = val
#
#     def calc_v(self, m):  # вычисление обьема жидкости, соответствующего заданной массе
#         res = m / self._density
#         print(f"Обьем {m} кг {self._name} равен {res} m^3/")
#         return res
#
#     def calc_m(self, v):  # Вычисление массы жидкости соответствующее заданному обьему
#         res = v * self._density
#         print(f"Вес {v} m^3 {self._name} составляет {res} кг.")
#         return res
#
#     def print_info(self):
#         print(f"Жидкость {self._name} плотность = {self._density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength # крепость
#
#     def edit_strength(self, val):
#         self.strength = val
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# ========================================================================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):  # спецом чтоб использовать в наследовании, для получения определенных данных
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point):
#
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()

# ====================================================================================================

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", {self.fon})
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", {self.border})
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()
# =====================================================================================

# 66 урок - 31 в реале

# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # f = ["Фамилия", "Имя", "Отчество"]
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # "ФамилияИмяОтчество"
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должне быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate("Волков Игорь Николаевич", 19, "1234 567890", 80)
# p1.fio = "Соболев Игорь Николаевич"
# p1.weight = 60
# p1.password = "4567 123456"
# p1.old = 35
# print(p1.__dict__)
# ==============================================================================

# Перегрузка методов 66-31

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()
# line.set_coords(Point(3, 4), Point(1, 2))
# line.draw_line()
# ======================================================================

# 66-31

# from abc import ABC, abstractmethod


#
#
# # абстрактный класс
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигру")
#
#     @abstractmethod
#     def move(self):  # абстрактный метод
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()
# from math import pi
#
#
# from math import pi
#
# class Table:
#
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# t.set_sides(2)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = Round_table(radius=10)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = Round_table(radius=20)
# t2.set_radius(60)
# print(t2.__dict__)
# print(t2.calc_area())

# ===================================================================================================

# 57-35 урок Полиморфизм Функторы

# Создать иерархию классов: Human(Человек),  Student(Студент),
# Teacher(Преподаватель), Graduate(Дипломник).
# Создать список группы представителей данной иерархии,
# и вывести информацию о каждом участнике

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"{self.last_name} {self.first_name} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, spec, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, experience, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         print(f"{self.speciality} {self.experience}", end=" ")
#         super().info()
#
# class Graduate(Student):
#     def __init__(self, topic, spec, group, rating, last_name, first_name, age):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
# ]
#
# for i in group:
#     i.info()

# ==============================================================================================
# РАЗНЫЕ ВСТРОЕННЫЕ магические методы

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, 2, -7)
# print(len(p))
# print(dir(Point))
# print(p.__dict__)
# print(abs(p))

# =========================================================================================

# SLOTS супер тема для экономии веса проги

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')  # слотс это свойства с какими именами могут присутствовать в нашем классе
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter # в закрытую переменную __length получаем доступ через сеттер
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)

# ===========================================================================================

# ВАЖНЫЙ МОМЕНТ  особенности работы коллекции слотс при наследовании классов

# class Point:
#     __slots__ = ('x', 'y')  # слотс это свойства с какими именами могут присутствовать в нашем классе
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z', # запятая для наследия от кортежа
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
#
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)

# ===========================================================================================

# возможность работы с классом как с функцией это ФУНКТОРЫ !

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         # return self.__counter
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter() # у нового экземпляра свой счетчик
# c2()
# c2()
# c2()
# ===================================================================================
# РЕАЛИЗУЕМ ФУНКТОР ДЛЯ УДАЛЕНИЯ ВВЕДЕННЫХ ЗНАКОВ
# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripsChars("?;:!. ")
# print(s1(" ?HelloWorld! "))

# БЫЛИ ЕЩЕ МОМЕНТЫ С ИСПОЛЬЗОВАНИЕМ КЛАССОВ КАК ДЕКОРАТОРОВ
# ===================================================================================

# из урока 58-32 АБСТРАКТНЫЕ МЕТОДЫ - ЕСЛИ В КЛАССЕ ЕСТЬ ХОТЯ БЫ 1 АБСТР
# МЕТОД ТО КЛАСС СТАНОВИТСЯ АБСТР-НЫМ АВТОМАТИЧЕСКИ

# Создайте базовый абстрактный класс "Валюта" для работы с денежными
# суммами. Определите методы перевода значения в рубли
# и вывода на экран. Реализуйте производные классы "Доллар" и
# "Евро" c собственными методами перевода в рубли и вывода на экран.
# ПРИДУМАТЬ САМОСТАЯТЕЛЬНО какими свойствами будет обладать каждый из классов,
# и какие методы сделать абстрактными

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 72.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 93.34
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for i in d:
#     i.print_value()
#     print(f" = {i.convert_to_rub():.2f} RUB")# красиво округлили внутри фигурных скобок за счет f строки
#
# print("*" * 50)
# for i in e:
#     i.print_value()
#     print(f" = {i.convert_to_rub():.2f} RUB")

# ===================================================================================

# ИНТЕРФЕЙС


# многого не записал. урок 58-32 55минута МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("я - метод внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name):
#             self.inner_name = inner_name
#
#         def inner_method(self):
#             print("я - метод внутреннего класса")
#             MyOuter.outer_class_method()
#             print(MyOuter.age )
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний")
# inner.inner_method()

# ==================================================================================
# не особо важно но такие конструкции бывают
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Emplloyee list")
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print("Degree:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alex"
#             self.id = '234'
#
#         def display(self):
#             print('Name:', self.name)
#             print("Degree:", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
#
# d2 = outer.head
# d2.display()
# =================================================================================

# Для чего вообще применяются вложенные классы ?!

# class OS:
#     def system(self):
#         return "Windows 10"
#
#
# class CPU:
#     def make(self):
#         return "Intel"
#
#     def model(self):
#         return "Core-i7"
# =================================================================================

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# некоторые вещи из 58 урока остались не записанными
# ================================================================================

# урок 59 Классы, Перезагрузка операторов, Продолжение(дз в файле fakeDZ.py)

# МИКСИНЫ - (Mixins)/ ПРИМЕСИ - РАБОТАЮТ ПО ПРИНЦИПУ МНОЖЕСТВЕННОГО НАСЛЕДОВАНИЯ

# основная цель миксинов(родительский класс) предоставить методы(такие классы котоорые сами по себе не используются)

# class Displyer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displyer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displyer): # дочерний класс который наследуется от двух верхних классов
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
# sub = MySubClass()
# sub.display("Это строка будет отображаться и записываться в файл")

# ЕЩЕ ОДИН ПРИМЕР МИКСИНОВ УРОК 59 49МИН02СЕК>>
# ПЕРЕГРУЗКА ОПЕРАТОРОВ 1Ч 20МИН

# class Clock:
#     __DAY = 86400  # 24*60*60
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other): # метод для сложения текущего экземпляра класса с другим таким же
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return  Clock(self.__secs + other.__secs)
#
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2
# print(c3.get_format_time())


# ================================================================================

# МАГИЧЕСКИЕ МЕТОДЫ ОПЕРАТОРОВ PYTHON

# class Clock:
#     __DAY = 86400  # 24*60*60
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):  # метод для сложения текущего экземпляра класса с другим таким же
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs + other.__secs)
#
#     def __sub__(self, other):  # для действия -= МЕТОД БУДЕТ isub
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs - other.__secs)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs * other.__secs)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs // other.__secs)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs % other.__secs)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c3 = Clock(300)
# c1 = c1 + c2 + c3
# print("c1: ", c1.get_format_time())
# c4 = c1 - c2
# print("c1 - c2", c4.get_format_time())
# c4 = c1 * c2
# print("c1 * c2", c4.get_format_time())
# c4 = c1 % c2
# print("c1 % c2", c4.get_format_time())
# c4 = c1 // c2
# print("c1 // c2", c4.get_format_time())


# ================================================================================
# МАГИЧЕСКИЕ МЕТОДЫ СРАВНЕНИЯ PYTHON

# class Clock:
#     __DAY = 86400  # 24*60*60
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):  # метод для сложения текущего экземпляра класса с другим таким же
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом Clock")
#
#         return Clock(self.__secs + other.__secs)
#
#     def __eq__(self, other):  # метод оператора сравнения РАВНО
#         return self.__secs == other.__secs
#
#     def __ne__(self, other):
#         return self.__secs != other.__secs
#
#
# c1 = Clock(200)
# c2 = Clock(20)
# print(c1.get_format_time())
#
# if c1 == c2:
#     print("Время одинаковое")
# else:
#     print("Время разное")
#
# if c1 != c2:
#     print("они не равны")
# else:
#     print("Они равны")

# ================================================================================

# У Р О К 60  ПЕРЕГРУЗКА ОПЕРАТОРОВ ПРОДОЛЖЕНИЕ
# работа с квадратными скобками, к примеру передавать список данных

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # перегрузим возможность получения данных в кв-ых скобках
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):  # для присвоения нового значения
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Вася", [5, 5, 3, 4, 5])
# print(s1[1])
# s1[4] = 2
# del s1[2]
# print(s1[0])

# ================================================================================
# урок 60-34 43мин
# Напишите класс Point3D для хранения в трехмерном пространстве(x, y ,z) + методы, стат методы, перегрузку операторов

# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):  #
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)  # isinstance(v, (int, float))
#
#     @staticmethod
#     def __check_zero(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("Ни одна из координат второго операнда не должна быть равна нулю")
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check_zero(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):  # self - экземпляр класса, item - значение координаты
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print("Координаты должны быть числами")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f"Координаты 1-й точки: {pt1}")
# print(f"Координаты 2-й точки: {pt2}")
#
# pt3 = pt1 + pt2
# print(f"Сложение координат: ({pt3})")
# pt3 = pt1 - pt2
# print(f"Вычитание координат: ({pt3})")
# pt3 = pt1 * pt2
# print(f"Умножение координат: ({pt3})")
# pt3 = pt1 / pt2
# print(f"Деление координат: ({pt3})")
# print(f"Равенство координат: {pt1 == pt2}")
#
# print("x = ", pt1['x'], "x1 =", pt2['x'])
# print("y = ", pt1['y'], "y1 =", pt2['y'])
# print("z = ", pt1['z'], "z1 =", pt2['z'])
#
# pt1['x'] = 20
# print("Запись значения в координату x:", pt1['x'])
# print(f"Координаты 1-й точки: {pt1}")

# ================================================================================

# у р о к 60 ПОЛИМОРФИЗМ возможность работы
# с совершенно разными обьектами языка питон единым образом

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(5)
# s2 = Square(20)
#
# shape = [r1, r2, s1, s2]  # список разных экземпляров разных классов!!!
#
# for g in shape:
#     print(g.get_perimetr())
# ================================================================================

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  # len("Python35")
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))  # 45
# print(t2.total(35))  # 8
# ================================================================================

# урок 60 полиморфизм

#  ЗАДАЧА Создайте два класса Cat Dog Реализуйте методы
# 4 MIN
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# ================================================================================

# у р о к 61 МодулИ про создание папки с дыркой

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def __repr__(self):
#         return f"{self.__class__}{self.w}{self.h}"
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for i in shape:
#     print(i.get_perimetr())

# ================================================================================

# Из папки авто из классов вызовим методы(для экземпляра дочернего класса),
# один метод от родит-го класса, другой от дочернего

# from avto import electroavto
#
#
# def main():
#     e = electroavto.ElectroAvto("Tesla", "T", 2018, 99000)
#
#     e.show_avto()
#     e.description_battery()
#
#
# if __name__ == "__main__":
#     main()
# ==================================================================================
#  61-37 урок

# from paket import circle
# from paket import rectangle
# from paket import cylinder
#
# circles = [circle.Circle(4), circle.Circle(2)]

# ================================================================================

# 62-38 У Р О К (упаковка данных)
# СЕРИАЛИЗАЦИЯ - (кодирование) запись данных на диск (c вложенными функциями будет сложновато)
# ДЕСЕРИАЛИЗАЦИЯ - (декодирование) чтение данных
# Сторонние модули сериализации

# В СТАНДАРТНОЙ БИБЛИОТЕКЕ(для кодирования и декодирования) Python:
# - marshal
# - pickle(только с питоном работает)
# 1 dump() - сохраняет данные в файл
# 2 load() - считывает данные из файла

# dumps() - сохраняет данные в оперативную память
# loads() - считывает данные из оперативной паммяти
# - json
# 1 dump() - сохраняет данные в файл
# 2 load() - считывает данные из файла

# dumps() - сохраняет данные в оперативную память
# loads() - считывает данные из оперативной паммяти

# biblioteki - папка про это
# avto peket - папки про то как использовать модули + модули с наследованием классов

# ========================================================================

# import pickle


# filename = 'basket.txt'
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, "rb") as fh:
#     print(pickle.load(fh))

# =================================================================================

# import pickle
#
#
# class Test:
#     a_number = 35
#     a_string = "привет"
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\nСтрока: {Test.a_string}\nСпискок: " \
#                f"{Test.a_list}\nКортеж: {Test.a_tuple}" \
#                f"\nСловарь: {Test.a_dict}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в сторку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация в сторку:\n{l_obj}\n")

# ==========================================================

# import pickle
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         print(attr)
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# =======================================================================
# 62-38

# import pickle
#
#
# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("moments.txt")
# print(reader.red_line())
# print(reader.red_line())
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())

# =============================================================
# 62-38 1:51:02

import json

# data = {
#     'firstName': "Jane",
#     'lastName': "Djo",
#     'hobbies': ("running", "sky diving"),
#     'age': 5,
#     "20": "one"
# }

# with open("data_file.json", "w") as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", "r") as fw:
#     print(json.load(fw))

# st = json.dumps(data, sort_keys=True)
#
# data = json.loads(st)
# print(data)

# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# ===========================================================================
# 62-38 ЭТО ТО ЧТО НА ПАРЕ А НИЖЕ ТО ЧТО ДОМАШКА
#
# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'b', 'd', 'e', 'f', 'e', 'g']
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
#     print(person)
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

# ================================================================================================================
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

# 67-39

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f"Студент {self.name}: {a[:-2]}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tmp = {"Students": stud_list}
#             data.append(tmp["Students"])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_journal(cls, file):
#         with open(file, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# Student.dump_to_json(st2, "student.json")
# Student.load_from_file("student.json")
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# print(my_group)
# Group.dump_group("group.json", my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# Group.upload_journal("group.json")
#
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
# Group.dump_group("group.json", my_group2)
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())

# ================================================================================


# ================================================================================
# 63-40 урок паттерны проектирования, принципы разделения паттернов

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_completed = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("data.json", "w") as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open("data.json", 'r') as f:
#     print(json.load(f))

# ================================================================================

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:  # {1: 2, 2: 1}
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_completed = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("data.json", "w") as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open("data.json", "r") as f:
#     print(json.load(f))

# ======================================================================


# 63-40 урок csv (comma separated values) - для работы с огромным кол-ом данных

# csv.reader
# csv.writer
# csv.DictReader
# csv.DictWriter

# у этого модуля есть константы!!!


# ================================================================================
# 63-40
import csv

# with open("data.csv") as f:
#     reader = csv.reader(f, delimiter=",")
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# with open("data.csv") as f:
#     fields_name = ["Имя", "Профессия", "Год рождения"]
#     reader = csv.DictReader(f, fieldnames=fields_name)  # delimiter=","
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. ", end="")
#         print(f"Родился в {row['Год рождения']} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# with open("student.csv", mode="w") as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])
# ================================================================

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", 'w') as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open("sw_data.csv") as f:
#     print(f.read())

# with open("sw_data.csv", 'w') as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)
#
# with open("sw_data.csv") as f:
#     print(f.read())

# with open("student1.csv", mode="w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), lineterminator="\r")
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# from bs4 import BeautifulSoup
# import re

# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return False

#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})  # .text
# for i in row:
#     get_salary(i.text)

# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# row = soup.find("div", class_="name")  # find - возвращает первый найденный элемент
# row = soup.find_all("div", class_="name")  # find_all - возвращает все найденные элементы
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find("div", {"data-set": "salary"})
# alena = soup.find("div", text="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# ================================================================================
#  69-41

# import requests
#
# r = requests.get("https://ru.wordpress.org/")
# print(r.text)
# print(r.content)
# print(r.status_code)
# print(r.headers)
# print(r.headers['content-type'])

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))


# if __name__ == '__main__':
#     main()
# import re
# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find_all("section", class_="plugin-section")[1]
#     plugins = s.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#         return plugins
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import csv
# from bs4 import BeautifulSoup
# import requests
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("plugins1.csv", 'a', encoding="utf-8") as f:
#         writer = csv.writer(f, lineterminator="\r")
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['active'],
#                          data['cy']))
#
#
# def refine_cy(s):
#     return s.split(" ")[-1]
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#         try:
#             url = el.find("h3").find('a').get('href')
#         except ValueError:
#             url = ""
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ""
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(22, 26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parse import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/type/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# from bs4 import BeautifulSoup
# import requests
# import re
#
#
# class Parser:
#     html = ""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")  # []
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r"\D", "", pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r"\D", "", pr2)
#             if price_2.isnumeric():  # содержит ли строка только числа
#                 prices.append((int(price_1) + int(price_2)) / 2)
#             else:
#                 prices.append(int(price_1))
#
#         print(prices)
#         print(f"Средняя цена: {round(sum(prices) / len(prices))} руб.")
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
#
# pars = Parser(f"https://www.e-katalog.ru/list/206/")
# pars.run()

# from bs4 import BeautifulSoup
# import requests
# import re
#
#
# class Parser:
#     html = ""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")  # []
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r"\D", "", pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r"\D", "", pr2)
#             if price_2.isnumeric():  # содержит ли строка только числа
#                 prices.append((int(price_1) + int(price_2)) / 2)
#             else:
#                 prices.append(int(price_1))
#         return sum(prices) / len(prices)
#
#     def run(self):
#         self.get_html()
#         return self.parsing()
#
#
# av = []
# for i in range(18):
#     pars = Parser(f"https://www.e-katalog.ru/list/206/{i}/")
#     av.append(pars.run())
#
# # print(av)
# print(f"Средняя цена: {round(sum(av) / len(av), 2)} руб.")

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split(' ')
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Method Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200  # \n\n
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Not Found</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()  # 127.0.0.1:5000
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     while True:
#         run()


# import sqlite3 as sq
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
# cur.execute("""
# CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# summa REAL,
# data TEXT
#  )
# """)


# import sqlite3 as sq
#
# cars = [
#     ('BWM', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()
# con.close()


# import sqlite3 as sq
#
# cars = [
#     ('BWM', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT car_id, model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(2)
#     # print(rows)
#
#     for res in cur:
#         print(res['car_id'], res['model'], res['price'])


# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))


# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()

# with open("sql_dump.sql", "r") as f:
#     sql = f.read()
#     cur.executescript(sql)

# with open("sql_dump.sql", "w") as f:
#     for sql in con.iterdump():
#         f.write(sql)

# for sql in con.iterdump():
#     print(sql)


# import sqlite3 as sq
#
# data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]
#
# con = sq.connect(":memory:")
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT
#     )""")
#
#     cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())

# ================================================================================


# ================================================================================


# ================================================================================


# ================================================================================
from random import randint

lst = sorted([randint(1, 99) for i in range(10)])

print(lst)
k = int(input("Введите число: "))


def binary_search(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high) // 2

        if data[middle] == elem:
            return f"Число {elem} в списке присутствует"
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return f"Число {elem} в списке отсутствует"


print(binary_search(lst, k))
