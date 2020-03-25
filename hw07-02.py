# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

MIN_EL = 0
MAX_EL = 50
SIZE = 20

array = [random.uniform(MIN_EL, MAX_EL) for i in range(SIZE)]


def merge_sort(unsorted_array):
    def split_arr(arrays):  # подфукция разделения исходного массива на подмассивы длиной <=2 элементов
        for arr in arrays:
            if len(arr) > 2:
                split_point = len(arr) // 2
                arrays.append(arr[:split_point])
                arrays.append(arr[split_point:])
                arrays.remove(arr)
                split_arr(arrays)  # рекурсия!!
            elif len(arr) == 2:  # тут же добавляем сортировку подмассивов длиной в 2 элемента
                if arr[0] > arr[1]:
                    arr[0], arr[1] = arr[1], arr[0]
        return arrays

    def merge(arr1, arr2):  # подфункция слияния массивов
        arr1_idx = 0
        arr2_idx = 0
        sum_arr = []
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        while arr1_idx < len(arr1):
            if arr1[arr1_idx] < arr2[arr2_idx]:
                sum_arr.append(arr1[arr1_idx])
                arr1_idx += 1
                if arr1_idx == len(arr1):
                    sum_arr += arr2[arr2_idx:]
                    return sum_arr
            else:
                sum_arr.append(arr2[arr2_idx])
                arr2_idx += 1
                if arr2_idx == len(arr2):
                    sum_arr += arr1[arr1_idx:]
                    return sum_arr
        return sum_arr

    array_ini = [unsorted_array]  # исходный массив переделываем в элемент массива
    array_spl = split_arr(array_ini)  # разделяем исходный массив на набор отсортированных массивов

    while len(array_spl) > 1:  # сливаем массивы в один отсортированный
        array_spl.append(merge(array_spl.pop(), array_spl.pop()))

    return array_spl[0]


print(array)
print(merge_sort(array))
