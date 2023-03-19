"""Напишите программу для печати всех уникальных значений в словаре"""

list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Вариант 2
unique_kyes = set()
for value in list_1:
    unique_kyes.update(value.values())
print(unique_kyes)
