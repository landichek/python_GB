"""Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два прямоугольника)."""

n = int(input("Введите количество долек вдоль: "))
m = int(input("Введите количество долек поперек: "))
k = int(input("Сколько долек хотите отломить: "))

if k % m == 0 or k % n == 0:
  print("Можно")

else:
  print("Нельзя")
