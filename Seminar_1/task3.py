"""В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них"""

a = 20  # кол-во человек в 1 классе
b = 21  # кол-во человек в 2 классе
c = 22  # кол-во человек в 3 классе

s1 = (a + 1) // 2
s2 = (b + 1) // 2
s3 = (c + 1) // 2

print(s1 + s2 + s3)