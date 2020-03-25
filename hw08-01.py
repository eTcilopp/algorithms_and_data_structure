# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различныхподстрок
# в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# func("papa")
# 6
# func("sova")
# 9


def owl(word):
    array = []
    for i in range(len(word) + 1):
        for j in range(1, len(word) + 1 - i):
            array.append(hash(word[i:i + j]))
    return len(set(array)) - 1


print(owl('kolbasa'))

if __name__ == '__main__':
    assert owl('papa') == 6
    assert owl('sova') == 9
