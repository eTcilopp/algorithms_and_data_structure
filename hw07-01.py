#  Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
#  заданный случайными числами на промежутке [-100; 100).
#  Выведите на экран исходный и отсортированный массивы.
#
# Шейкер-сортировка не применялась.

import random

MIN_EL = -100
MAX_EL = 100
SIZE = 10

array = [random.randrange(MIN_EL, MAX_EL) for i in range(SIZE)]
print(array)


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        exchange_cnt = 0
        exchange_idx = len(arr) - 1
        for i in range(exchange_idx):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                exchange_cnt += 1
                exchange_idx = i  # отпимизация № 2. Запоминаем иднекс, где произошла последняя перестановка
        if exchange_cnt == 0:  # оптимизация №1 алгоритма для естественного поведения. Нет перестановок - конец работы.
            return arr
        n += 1
    return arr


print(bubble_sort(array))
