"""Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива"""

first_numbers = [3, 1, 3, 4, 2, 4, 12]
second_numbers = [4, 15, 43, 1, 15, 1]

count = 0

for i in range(len(first_numbers)):
    for i in range(len(second_numbers)):
        if first_numbers[i] == second_numbers[j]:
            count += 1
    if count == 0:
        print(first_numbers[i])
    count = 0

#Вариант 2:

count = 0
for first_num in first_numbers:
    for second_num in second_numbers:
        if first_num == second_num:
            count += 1
    if count == 0:
        print(first_num)
    count = 0

#Вариант 3:

for i in range(len(first_numbers)):
    if first_numbers[i] not in second_numbers:
        print(first_numbers[i], end=' ')
