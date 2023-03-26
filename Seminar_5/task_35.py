"""Даны два целых числа А и В.
Выведите все числа от А до В включительно. В порядке возрастания,
если А < В. В порядке убывания если A > B """

def print_number(a, b):
    if a == b:
        return f"{a}"
    if a > b:
        return f"{a}, {print_number(a - 1, b)}"
    if a < b:
        return f"{a}, {print_nmber (a+1, b)}"

print(print_number(1, 10))