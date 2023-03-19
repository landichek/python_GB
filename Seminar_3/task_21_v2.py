"""Напишите программу для печати всех уникальных значений в словаре"""

list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Вариант 1 - Modified
unique_kyes = set()
for dict_item in list_1:
    for value_dict in dict_item.values():  # Сразу получи значения словаря, а не его ключ
        unique_kyes.add(value_dict)  # Кладём значение без обрашения по ключу (dict_item[key])
print(unique_kyes)
