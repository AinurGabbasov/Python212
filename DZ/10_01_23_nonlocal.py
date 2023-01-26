# Локальная переменная

def paralelp_square(a, b, c):
    def rec_square(i, j):
        return i * j

    s = 2 * (rec_square(a, b) + rec_square(a, c) + rec_square(c, b))
    return s


print(paralelp_square(2, 4, 6))
print(paralelp_square(5, 8, 2))
print(paralelp_square(1, 6, 8))

# =====================================================================================

# Глобальная переменная

# s = 0
# def paralelp_square(a, b, c):
#     def rec_square(i, j):
#         return i * j
#     global s
#     s = 2 * (rec_square(a, b) + rec_square(a, c) + rec_square(c, b))
#     return s
#
#
# print(paralelp_square(2, 4, 6))
# print(paralelp_square(5, 8, 2))
# print(paralelp_square(1, 6, 8))

# =====================================================================================

# Нелокальная переменная

# def paralelp_square(a, b, c):
#     s = 0
#
#     def rec_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rec_square(a, b) # при вызове к s добавляется площадь прямоугольника
#     rec_square(a, c) # при вызове к s добавляется площадь прямоугольника
#     rec_square(c, b) # при вызове к s добавляется площадь прямоугольника
#     return 2 * s # в итоге эти три сложенных прямоугольника умножим на 2 и получим общую площадь
#
#
# print(paralelp_square(2, 4, 6))
# print(paralelp_square(5, 8, 2))
# print(paralelp_square(1, 6, 8))