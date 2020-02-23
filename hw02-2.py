# Задача 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, #  в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).
#
# https://drive.google.com/file/d/10WcNpYDk9EndgWAFgmzuGbn1YfRkH5wd/view?usp=sharing

print('Введите натуральное число')
n = input()
odd = 0
for el in n:
    if int(el) % 2:
        odd += 1
print(f'четных чисел: {len(n) - odd}\nнечетных чисел: {odd}')
