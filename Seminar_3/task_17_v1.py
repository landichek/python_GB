"""Дан список чисел. Определите сколько в нем встречается различных чисел"""

import random

s = [random.randint(0, 100) for _ in range(10)]  ##random.randint - функция через которую создаем список из рандомных чисел. 
## Вместо i ставим _ Так пайтон понимаем что это переменная не так важна и не нужна нам и будет выкидвать из памяти
result = []

for num in s:
    if result.count(num) == 0:
        result.append(num)
print(result)
print(len(result))
