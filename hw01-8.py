# Задача 8. Определить, является ли год,
# который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/1njb-VQUyYxyuodYFTC75rRgGqg-1Iqor/view?usp=sharing

print('Введите год для проверки на високосность')
y = int(input())
if y % 4 != 0:
    print('Это обычный год, не високосный')
elif y % 100 == 0:
    if y % 400 != 0:
        print('Это обычный год, не високосный')
    else:
        print('Это високосный год')
else:
    print('Это високосный год')
