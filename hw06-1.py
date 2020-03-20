# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# Выбран алгоритм поиска простых чисел.

# Python 3.7.4 [MSC v.1916 32 bit (Intel)]
# OS: microsoft Windows 8.1 Pro  Ver. 6.3.9600 Build 9600; 64 Bit


import math
import timeit
import cProfile
import sys


def memory_use(*variables):  # функция для замера объема памяти, занятой под переменные
    memory_usage = 0
    for var in variables:
        memory_usage += sys.getsizeof(var)
    return f'** Для хранения переменных использовано {memory_usage} байт(а) памяти.'


def test_func(func):  # функция для проверки работоспособности функций
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        # print(memory_use(func, i, item, lst))
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
    # print(memory_use(n, num))
    return int(round(n))


# Решето Эратосфена

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

    # print(memory_use(a, b, i, j, m, n, num))
    return b[num - 1]


def my_func(num):  # алгоритм поиска простых чисел простым перебором.
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
    # print(memory_use(el, i, n, num))
    return el


# Python program to display all the prime numbers within an interval

def my_func2(num):
    if num < 3:
        return num + 1
    primes = []
    check = 2
    while len(primes) < num:
        prime_test = [check for i in primes if check % i == 0]
        primes += [] if prime_test else [check]
        check += 1
    # print(memory_use(check, num, prime_test, primes))
    return primes[-1]

# Тестирование
# test_func(sieve)
# test_func(my_func)
# test_func(my_func2)

# print(sieve(999))
# print(my_func(999))
# print(my_func2(999))


# Результаты замеров использования памяти:

# Python 3.7.4 [MSC v.1916 32 bit (Intel)]
# OS: microsoft Windows 8.1 Pro  Ver. 6.3.9600 Build 9600; 64 Bit

# Алгоритим № 1
# sieve(999) - Для хранения переменных использовано 30 + 37740 = 37770 байт памяти.
# Время 0.731480734
# Сложность O(n**3)

# Алгоритм № 2
# my_func(999) - Для хранения переменных использовано 56 байтов памяти
# Время 354.032368265
# Сложность O(n**3)

# Алгоритм № 3
# my_func2(999) - Для хранения переменных использовано 4580 байт(а) памяти.
# Время 43.45941831800002
# Сложность O(n**2)

# Вывод: Реализация Решета Эратосфена представляется наиболее эффективной с т.з. быстродействия
# и наименее эффективной с т.з. расходования памяти. Выигрыш в быстродействии значителен
# и компенсирует повышенный расход памяти.
# Вариант 2 малопригоден из-за низкого быстродействия, но привлекателен с т.з. расхода памяти.
# Вариант 3 представляет собой оптимизированный вариант 2, при котором за счет запоминания
# промежуточных значений (повышение расхода памяти) удается повысить быстродействие.
#
# Общий вывод: следует использовать алгоритм 1 до тех пор, пока не начнет проявляться
# нехватка памяти. После чего можно использовать алгоритм 3


# print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.027160312000000006
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.055062867000000015
# print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.13194798400000002
# print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.32175169400000003
# print(timeit.timeit('sieve(999)', number=100, globals=globals()))  # 0.731480734

# print(timeit.timeit('my_func(50)', number=100, globals=globals())) # 0.452236105
# print(timeit.timeit('my_func(100)', number=100, globals=globals())) # 2.53319347
# print(timeit.timeit('my_func(200)', number=100, globals=globals())) # 14.897041703000001
# print(timeit.timeit('my_func(400)', number=100, globals=globals())) # 78.11904733099999
# print(timeit.timeit('my_func(999)', number=100, globals=globals())) # 354.032368265

# print(timeit.timeit('my_func2(50)', number=100, globals=globals())) # 0.08037122899999999
# print(timeit.timeit('my_func2(100)', number=100, globals=globals())) # 0.361892322
# print(timeit.timeit('my_func2(200)', number=100, globals=globals())) # 1.572940408
# print(timeit.timeit('my_func2(400)', number=100, globals=globals())) # 6.265903637999999
# print(timeit.timeit('my_func2(999)', number=100, globals=globals())) # 43.45941831800002
