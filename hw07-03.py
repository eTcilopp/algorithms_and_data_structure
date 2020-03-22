# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

MIN_EL = -100
MAX_EL = 100
SIZE = 111

array = [random.randrange(MIN_EL, MAX_EL) for i in range(SIZE)]


def find_median(src_array):
    assert len(src_array) % 2 != 0, 'Массив содежит четное число элементов, что противоречит условиям задачи'
    mid_point = len(src_array) // 2 + 1
    min_diff = len(src_array)
    median_candidate = ''
    for el in src_array:
        not_less = 0
        not_more = 0
        for sub_el in src_array:
            if sub_el >= el:
                not_less += 1
            if sub_el <= el:
                not_more += 1
        if abs(not_more - not_less) < min_diff:
            min_diff = abs(not_more - not_less)
            median_candidate = el
        if not_more > mid_point | not_less > mid_point:
            break
    return median_candidate


print(array)
print(find_median(array))

if __name__ == '__main__':
    assert find_median([4, 8, 2, 6, 1]) == 4
    assert find_median([4, 8, 4, 4, 6]) == 4
    assert find_median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert find_median([10, 2, 3, 4, 5, 6, 7, 8, 9]) == 6
    assert find_median([1, 1, 1, 1, 2]) == 1
