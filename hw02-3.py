# Задача 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.
#
# https://drive.google.com/file/d/10WcNpYDk9EndgWAFgmzuGbn1YfRkH5wd/view?usp=sharing

print('Введите целое положительное число')
n = input()
s = 0
for i, el in enumerate(n):
    s += int(el) * 10 ** i
print(s)
