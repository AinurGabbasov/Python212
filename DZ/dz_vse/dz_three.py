#  КАЛЬКУЛЯТОР ПИТОН

print("""
Выберите операцию: 
1 - "r" - применяет унарный минус к операнду(первому введенному числу) 
2 - "+" - сложение
3 - "-" - вычитание
4 - "/" - деление
5 - "*" - умножение
6 - "%" - остаток от деления
7 - "<" - минимальное из двух чисел
8 - ">" - максимальное из двух чисел
9 - "**" - первое число возводится в степень второго числа""")
try:
    oper = int(input("Введите выбранную операцию(цифру): "))
    if 0 < oper < 10:
        a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
        if oper == 1:
            print(a * -1)
        elif oper == 2:
            print("Сумма равна:", a + b)
        elif oper == 3:
            print("Разность равна:", a - b)
        elif oper == 4:
            try:
                print("Частное равно:", a / b)
            except (ZeroDivisionError):
                print("Нельзя делить на 0!")
        elif oper == 5:
            print("Произведение равно:", a * b)
        elif oper == 6:
            try:
                print("Остаток от деления равен:", a % b)
            except (ZeroDivisionError):
                print("Нельзя делить на 0!")
        elif oper == 7:
            print("Минимальное из двух чисел равно:",
                  "\n(Начните сначала, но введите разные числа)" if a == b else a if a < b else b)
        elif oper == 8:
            print("Максимально из двух чисел равно:",
                  "\n(Начните сначала, но введите разные числа)" if a == b else a if a > b else b)
        elif oper == 9:
            print(a, "в степени", b, "равно", a ** b)
    else:
        print('Не верно выбрана операция')
except (ValueError):
    print("Начните сначала, но введите целое число")

# # ДЛЯ ВЕЩЕСТВЕННЫХ ЧИСЕЛ
# try:
#     oper = int(input("Введите выбранную операцию(цифру): "))
#     if 0 < oper < 10:
#         a, b = float(input("Введите первое число: ")), float(input("Введите второе число: "))
#         if oper == 1:
#             print(a * -1)
#         elif oper == 2:
#             print("Сумма равна:", a + b)
#         elif oper == 3:
#             print("Разность равна:", a - b)
#         elif oper == 4:
#             try:
#                 print("Частное равно:", a / b)
#             except (ZeroDivisionError):
#                 print("Нельзя делить на 0!")
#         elif oper == 5:
#             print("Произведение равно:", a * b)
#         elif oper == 6:
#             try:
#                 print("Остаток от деления равен:", a % b)
#             except (ZeroDivisionError):
#                 print("Нельзя делить на 0!")
#         elif oper == 7:
#             print("Минимальное из двух чисел равно:",
#                   "\n(Обновите и введите разные числа)" if a == b else a if a < b else b)
#         elif oper == 8:
#             print("Максимально из двух чисел равно:",
#                   "\n(Обновите и введите разные числа)" if a == b else a if a > b else b)
#         elif oper == 9:
#             print(a, "в степени", b, "равно", a ** b)
#     else:
#         print('Не верно выбрана операция')
# except (ValueError):
#     print("Обновите и введите целое число")
