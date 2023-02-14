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
