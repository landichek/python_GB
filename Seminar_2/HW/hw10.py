"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть"""

n = int(input("Введите количество монеток: "))
count_zero = 0
count_one = 0

for i in range(n):
    x = int(input(f"Введите какой стороной лежит монета {i}: "))  # 0 - решка, 1 - орел
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f"Минимальное количество монет, которое нужно перевернуть: {count_zero}")
else:
    print(f"Минимальное количество монет, которое нужно перевернуть: {count_one}")
