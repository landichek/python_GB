"""Дана последовательность из N целых чисел и число К. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на К элементов
вправо, К - положительное число"""

import random

s = [random.randint(0, 100) for _ in range(10)]
s1 = s.copy ()  ## скопировала исходный массив, чтобы вывести два массива и посмотреть праивильно ли работает он

k = 3
k = k % len(s1) ## на данном этапе проверяем на сколько действительно раз надо сместить цикл. Если К будет огромным, например, 34456, мы мнооого раз будет возвращаться в исходное положение массива. 
## Чтобы не делать лишних действий и не тратить время, мы проверяем сколько действий мы делаем.

print (s)
print(s1[-k:] + s1[: -k]) ## сделали срез 3 элементов