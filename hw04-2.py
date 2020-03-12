# Задача 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов.

# Решето Эратосфена (276 - 194 до Н.Э.)
import math
import timeit
import cProfile


def test_func(func):  # функция для проверки работоспособности функций
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i + 1} OK')


def numbers_required(num):  # функция, вычисляющая сколько  нат. чисел нужно взять для поиска num простых чисел
    if num < 3:
        return 4
    n = num * math.log(num)
    if num < 4:
        n *= 2
    elif num <= 7:
        n *= 1.5
    elif num < 100:
        n *= 1.3
    elif num < 1000:
        n *= 1.2
    elif num < 10000:
        n *= 1.14
    elif num < 100000:
        n *= 1.13
    elif num < 1000000:
        n *= 1.121
    return int(round(n))


def sieve(num):  # алгоритм Решета Эратосфена
    n = numbers_required(num)
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b[num - 1]


def my_func(num):  # алгоритм поиска простых чисел простым же перебором.
    if num < 3:
        return num + 1
    el = 2
    i = 1
    while i < num:
        el += 1
        for n in range(el, 2, -1):
            if el % (n - 1) == 0:
                i -= 1
                break
        i += 1
    return el


# Тестирование
# test_func(sieve)
# test_func(my_func)


# print(sieve(80))
# print(my_func(80))


# print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.027160312000000006
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.055062867000000015
# print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.13194798400000002
# print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.32175169400000003
# print(timeit.timeit('sieve(800)', number=100, globals=globals()))  # 0.7902309319999999

# print(timeit.timeit('my_func(50)', number=100, globals=globals())) # 0.452236105
# print(timeit.timeit('my_func(100)', number=100, globals=globals())) # 2.53319347
# print(timeit.timeit('my_func(200)', number=100, globals=globals())) # 14.897041703000001
# print(timeit.timeit('my_func(400)', number=100, globals=globals())) # 78.11904733099999
# print(timeit.timeit('my_func(800)', number=100, globals=globals())) # 314.808900389999


# cProfile.run('sieve(200)') # метод append вызван 205 раз.

# cProfile.run('my_func(200)')
