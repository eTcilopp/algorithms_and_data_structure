# Задача 6. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.
# https://drive.google.com/file/d/1njb-VQUyYxyuodYFTC75rRgGqg-1Iqor/view?usp=sharing

print('Введите номер буквы в латинском алфавите')
char_num = int(input())
letter = chr(char_num + 96)
print(f'{letter}')
