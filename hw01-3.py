# Задача 3. По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
#
# https://drive.google.com/file/d/1njb-VQUyYxyuodYFTC75rRgGqg-1Iqor/view?usp=sharing
print('Введите координаты двух точек\nВведите координату x точки 1')
x1 = int(input())
print('Введите координату y точки 1')
y1 = int(input())
print('Введите координату x точки 2')
x2 = int(input())
print('Введите координату y точки 2')
y2 = int(input())
k = (y2 - y1) / (x2 - x1)
b = -(x2 * y1 - x1 * y2) / (x1 - x2)
print(f'Уравнение имеет вид\ny={k}x+{b}')
