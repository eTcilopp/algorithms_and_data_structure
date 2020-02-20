# 7. Напишите программу, доказывающую или проверяющую,
#  что для множества натуральных чисел выполняется равенство:
#  1+2+...+n = n(n+1)/2, где n — любое натуральное число.
#
# https://drive.google.com/file/d/10WcNpYDk9EndgWAFgmzuGbn1YfRkH5wd/view?usp=sharing

def recur_sum(n):
    if n == 1:
        return n
    else:
        return n + recur_sum(n - 1)


print('Введите число элементов множества n')
n = int(input())

s = recur_sum(n)

if s == n * (n + 1) / 2:
    print(f'Равенство подтверждено:\n1+2+...+n = n(n+1)/2, где n={n}: {s} = {int(n * (n + 1) / 2)}')
else:
    print(f'Равенство не подтверждено:\n1+2+...+n != n(n+1)/2, где n={n}: {s} = {int(n * (n + 1) / 2)}')
