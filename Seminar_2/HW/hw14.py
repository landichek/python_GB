"""Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N"""

N = int(input('Введите целое число больше 1: '))
k = 1
while k <= N:
    print(k, end=' ')
    k = k * 2