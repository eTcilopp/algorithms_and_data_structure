# Задача 8. Посчитать, сколько раз встречается определенная цифра в
# введенной последовательности чисел. Количество вводимых чисел и
# цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
#
# https://drive.google.com/file/d/10WcNpYDk9EndgWAFgmzuGbn1YfRkH5wd/view?usp=sharing


print('Сколько чисел будет введено?')
n = input()
print('Какую цифру нужно искать?')
target = input()

i = 1
count = 0
while i <= int(n):
    print(f'Введите число {i}:')
    num = input()
    count += num.count(target)
    i += 1
print(f'Цифра {target} встретилась {count} раз(а)')
