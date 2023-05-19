# ВЫВЕСТИ ПРЯМОУГОЛЬНИК ИЗ ЧЕРЕДУЮЩИХСЯ СИМВОЛОВ

simbol1, simbol2 = input("Введите первый символ: "), input("Введите второй символ: ")
a, b = int(input("Введите длину прямоугольника: ")), int(input("Введите ширину прямоугольника: "))

i = 1
while i < b + 1:
    if i % 2 == 0:
        k = 1
        while k < a + 1:
            print(simbol2, end='')
            k += 1
    else:
        k = 1
        while k < a + 1:
            print(simbol1, end='')
            k += 1
    print()
    i += 1

# ИЛИ ТАК
# if b == 1:
#     for i in range(a):
#         print(simbol1, end='')
#
# elif b % 2 == 0:
#     for i in range(b//2):
#         print(simbol1 * a)
#         print(simbol2 * a)
# else:
#     for i in range(b//2):
#         print(simbol1 * a)
#         print(simbol2 * a)
#     print(simbol1 * a)

