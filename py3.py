import random

a = {"Кола": 55, "Лук": 35, "Хлеб": 25, "Шашлык": 40, "Соль": 45, "ВИно": 20, "Водка": 30, "Палатка": 30}

maximum_load = 130
counter = 0
List_artibute = []
while counter < maximum_load:
    key, value = random.choice(list(a.items()))
    if key in List_artibute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    List_artibute += (str(key), str(value))

print(List_artibute, "=", counter)