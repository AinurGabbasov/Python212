# # Задача 1

# import re
#
#
# def validate_name(name):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ss_---_U@w0rd'))

# =================================================================
# Задача 2
# import re
#
# s = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
# reg = r'\d{2}/\d{2}/\d{4}'
# print(re.findall(reg, s))
