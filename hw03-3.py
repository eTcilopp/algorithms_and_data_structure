# Задача 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')

min_el = array[0]
max_el = array[0]
min_el_index = 0
max_el_index = 0

for i, el in enumerate(array):
    if el > max_el:
        max_el = el
        max_el_index = i
    elif el < min_el:
        min_el = el
        min_el_index = i

array[min_el_index], array[max_el_index] = array[max_el_index], array[min_el_index]

print('Измененный массив:')
print(array)
print(f'Поменяны местами элементы {min_el} и {max_el}')
