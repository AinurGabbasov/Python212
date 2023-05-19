# ПОСТРОИТЬ ЛИНИЮ

n = int(input("Укажите число символов: "))
tip = input("Укажите тип символа: ")
lin = int(input("Выберите ориентацию линии:\nвертикальная - 1 \nгоризонтальная - 0 : "))
i = 1
if lin == 0:
    while i <= n:
        print(tip, end='')
        i += 1
else:
    while i <= n:
        print(tip)
        i += 1
# # ИЛИ ТАК
# if lin == 1:
#     for i in range(n):
#         print(tip)
# else:
#     print(tip * n)
