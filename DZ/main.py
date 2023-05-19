"""Написать слово "КОПЕЕК" в правильном формате"""

num = int(input('Введите число от 1 до 99: '))

if 0 < num < 100:
    if 10 < num < 15:
        print(num, "копеек")
    elif 1 < num % 10 < 5:
        print(num, "копейки")
    elif num % 10 == 1:
        print(num, "копейка")
    else:
        print(num, "копеек")
else:
    print("Ошибка ввода данных")




