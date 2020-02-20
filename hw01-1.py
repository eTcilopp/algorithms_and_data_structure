# Задача 1. Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.
#
# https://drive.google.com/file/d/1njb-VQUyYxyuodYFTC75rRgGqg-1Iqor/view?usp=sharing

print('Введите целое трехзначное число')
a = int(input())
sum = a // 100 + a % 100 // 10 + a % 100 % 10
mult = a // 100 * a % 100 // 10 * a % 100 % 10
print(f'sum={sum}, mult={mult}')
