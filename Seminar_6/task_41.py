"""Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел."""

n = int(input())
list_first = []
for i in range(n):
    num = int(input())
    list_first.append(num)

count = 0
for i in range(1, n - 1):
    if list_first[i - 1] < list_first[i] < list_first[i + 1]:
        count += 1
print (count)

#Вариант 2:

list_first = [int(input("Элемент массива: ")) for _ in range (int(input("Кол-во элементов массива: ")))]
count = 0
for i in range(1, n - 1):
    if list_first[i - 1] < list_first[i] < list_first[i + 1]:
        count += 1
print (count)