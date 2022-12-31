# Задача № 1

a = ['red', 'green', 'blue']
b = ['#FF0000', '#008000', '#0000FF']
c = dict(zip(a, b))
print(c)

# Задача № 2

# new = {i: i**3 for i in range(1, 11)}
# print(new)

# Задача № 3

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# z = a | b | c
# print(z)

# Задача № 4

# a = {'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# a['emp3']['salary'] = 8500
# print(a)

# Задача № 5

# n = int(input("Количество студентов: "))
# students = {input(f'{i}-й студент: '): int(input("Балл: ")) for i in range(1, n + 1)}
# sr = int(sum(list(students.values())) / n)
# print("Средний балл: ", sr)
# print("Студенты с баллом выше среднего: ")
# for key, value in students.items():
#     if value > sr:
#         print(key)

# Задача № 6

# a = ['color', 'fruit', 'pet']
# b = ['blue', 'apple', 'dog']
# ab = {i: j for i, j in zip(a, b)}
# print(ab)
