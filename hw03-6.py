# Задача 6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# Условия задачи не объясняют действий при ситуации повтора максимально или минимального знаячений
# array = list(set(array))
print(f'Исходный массив:\n{array}')
max_el = array[0]
min_el = array[0]
max_i = 0
min_i = 0

for i, el in enumerate(array): # Ищем максимальное и минимальное значение в массиве
    if el > max_el:            # и их индексы
        max_el = el
        max_i = i
    elif el < min_el:
        min_el = el
        min_i = i
if min_i > max_i:
    min_i, max_i = max_i, min_i
array_sum = 0
for i in range(min_i + 1, max_i): # Суммируем значения элеменов массива между макс. и мин.значениями
    array_sum += array[i]
print(f'Сумма элементов, находящихся между\nминимальным({min_el}) и максимальным({max_el}) значениями равна {array_sum}')
