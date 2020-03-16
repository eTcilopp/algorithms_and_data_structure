# Задача 1.
# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
# для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Задача 3 из ДЗ 2 - ПРЕОБРАЗОВАНО В ФУНКЦИЮ
# Задача 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.
import timeit
import cProfile


# Вариант 1 (исходный)
def backward1(num):
    n = str(num)
    s = 0
    for i, el in enumerate(n):
        s += int(el) * 10 ** i
    return s


# print(timeit.timeit('backward1(123)', number=100, globals=globals())) # 0.00041900200000000165
# print(timeit.timeit('backward1(123456)', number=100, globals=globals())) # 0.0005910799999999938
# print(timeit.timeit('backward1(123456789876)', number=100, globals=globals())) # 0.0014676090000000017
# print(timeit.timeit('backward1(123456789876543210123456)', number=100, globals=globals())) # 0.0029759450000000007

# print(backward1(122345))

# Вариант 2
def backward2(num):
    n = 1
    while num // n > 10:
        n *= 10
    new_num = 0
    point = 1
    while n >= 1:
        new_num += num // n * point
        num -= num // n * n
        point *= 10
        n /= 10
    return int(new_num)


# print(backward2(12345))

# print(timeit.timeit('backward2(123)', number=100, globals=globals())) # 0.0003720389999999976
# print(timeit.timeit('backward2(123456)', number=100, globals=globals())) # 0.0008020490000000061
# print(timeit.timeit('backward2(123456789876)', number=100, globals=globals())) # 0.0016495929999999978
# print(timeit.timeit('backward2(123456789876543210123456)', number=100, globals=globals())) # 0.003942365999999996


# Вариант 3
def backward3(num):
    num = str(num)
    new_num = ''
    index = len(num)
    while index > 0:
        new_num += num[index - 1]
        index -= 1
    return int(new_num)


# print(backward3(12345))

# print(timeit.timeit('backward3(123)', number=100, globals=globals()))  # 0.0003360830000000009
# print(timeit.timeit('backward3(123456)', number=100, globals=globals()))  # 0.00032103900000000213
# print(timeit.timeit('backward3(123456789876)', number=100, globals=globals()))  # 0.000525036999999999
# print(timeit.timeit('backward3(123456789876543210123456)', number=100, globals=globals()))  # 0.0009572490000000003

# cProfile.run('backward1(123456789876543210123456)') #  Ничего не узнал, получаю спрошные нули.
# cProfile.run('backward2(123456789876543210123456)')
# cProfile.run('backward3(123456789876543210123456)')