# Задача 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')
frequency_arr = [0] * len(array)
most_repeats = 0
for i, el in enumerate(array):
    for sub_el in array:
        if type(sub_el) != str:
            if el == sub_el:
                frequency_arr[i] += 1
                array[array.index(sub_el)] = str(array[array.index(sub_el)])
        if frequency_arr[i] > most_repeats:
            most_repeats = frequency_arr[i]

print('Наиболее часто встречается число (числа):')
for i, freq in enumerate(frequency_arr):
    if freq == most_repeats:
        print(array[i], end=" ")
print(f'\nЧастота повторений = {most_repeats}')
