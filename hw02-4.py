# Задача 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
#
# https://drive.google.com/file/d/10WcNpYDk9EndgWAFgmzuGbn1YfRkH5wd/view?usp=sharing


print('Введите число элементов ряда n')
n = int(input())
s = 0

for i in range(0, n):
    s += 1 / (-2) ** i
print(f'Сумма ряда равна {s:.3f}')
