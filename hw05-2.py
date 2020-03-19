# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого —
# цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num1_h = list(input('Введите первое шестнадцатиричное число ').upper())[::-1]
num2_h = list(input('Введите второе шестнадцатиричное число ').upper())[::-1]
trans = 0
sum_result = []

if len(num1_h) > len(num2_h):
    num2_h.append('0' * (len(num1_h) - len(num2_h)))
if len(num1_h) < len(num2_h):
    num1_h.append('0' * (len(num2_h) - len(num1_h)))

for i in range(len(num1_h)):
    _res = HEX.index(num1_h[i]) + HEX.index(num2_h[i]) + trans
    if _res > 16:
        trans = 1
        sum_result.append(HEX[_res - 16])
    else:
        trans = 0
        sum_result.append(HEX[_res])
print(f'Сумма шестнадцатеричных чисел равна {sum_result[::-1]}')


# Вариант 2 (жульнический): Можно перевести числа в десятичную систему и выполнять операции с ними.
# Результат переводить в шестнадцатеричную систему.

def hex_to_dex(num_h):
    num_x = 0
    for edx, el in enumerate(num_h[::-1]):
        num_x += 16 ** edx * HEX.index(el)
    return num_x


def dex_to_hex(num_x):
    rest = []
    while num_x >= 16:
        rest.append(num_x % 16)
        num_x = num_x // 16
    rest.append(num_x)
    num_hex = []
    for el in rest[::-1]:
        num_hex.append(HEX[el])
    return num_hex


num1_h = list(input('Введите первое шестнадцатиричное число ').upper())
num2_h = list(input('Введите второе шестнадцатиричное число ').upper())
sum_h = dex_to_hex(hex_to_dex(num1_h) + hex_to_dex(num2_h))
mul_h = dex_to_hex(hex_to_dex(num1_h) * hex_to_dex(num2_h))

print(f'Сумма шестнадцатеричных чисел {num1_h} и {num2_h} равна {sum_h}')
print(f'Произведение шестнадцатеричных чисел {num1_h} и {num2_h} равна {mul_h}')
