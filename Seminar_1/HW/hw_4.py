"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?"""

s = int(input("Введите количество журавликов, которые сделали Петя, Катя и Сережа вместе: "))
a = s // 6  # вывела формулу. Это количество журавликов Пети и Сережи, так как они равны. s = a + a + 2 * (a + a)
c = 4 * a  # Катя сделала в два раза больше чем Петя и сережа вместе. с = 2 * (a + a)

print(f"Петя сделал: {a} журавликов, Сережа сделал {a} журавликов, Катя сделала {c} журавликов")
