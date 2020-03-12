# Задача № 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив:\n{array}')

min_a = array[0]
min_b = array[0]

for el in array:
    if el < min_a:
        min_b = min_a
        min_a = el
    elif el < min_b:
        min_b = el
print(f'Два наименьших элементов массива:\n1) {min_a}\n2) {min_b}')