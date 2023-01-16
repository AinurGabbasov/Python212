#  Задача 1

def func_compute(n):
    return lambda x: x * n


res = func_compute(2)
print(res(20))
print(res(15))

# ==================================================================================

#  Задача 2

# func = lambda x, y, z: x * y * z
#
# print(func(2, 5, 5))

# ==================================================================================

#  Задача 3

# sp = [{'name': 'Jennifer', 'final': 95},
#       {'name': 'David', 'final': 92},
#       {'name': 'Nikolas', 'final': 98}
#       ]
# print(sorted(sp, key=lambda x: x['name']))
# print(sorted(sp, key=lambda x: -x['final']))

# ==================================================================================

#  Задача 4

# sp = [{'name': 'Jennifer', 'final': 95},
#       {'name': 'David', 'final': 92},
#       {'name': 'Nikolas', 'final': 98}
#       ]
# print(max(sp, key=lambda x: x['final']))
# print(min(sp, key=lambda x: x['final']))