# Задача 1

# import re
#
#
# def vern_nomer(num):
#     reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$"
#     return re.findall(reg, num)
#
#
# print(vern_nomer('+7 499 456 45 78'))
# print(vern_nomer('+74994564578'))
# print(vern_nomer('7 (499) 456 45 78'))
# print(vern_nomer('7 (499) 456-45-78'))

# Задача 2

# def negative(a):
#     if len(a) == 0:
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print(n)
