# Задача 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

Enterprise = collections.namedtuple('Enterprise', 'name, sum_profit')
enterprises = []
cum_profit = 0
ent_num = int(input('Введите количество предприятий '))

for ent in range(ent_num):
    print()
    name = input(f'Введите наименование предприятия {ent + 1}')
    profit = {}
    sum_ent_profit = 0
    for q in range(1, 5):
        profit = float(input(f'Введите прибыль предприятия {name} за квартал № {q}'))
        sum_ent_profit += profit
    enterprises.append(Enterprise(name, sum_ent_profit))
    cum_profit += sum_ent_profit

glob_ave_profit = cum_profit / len(enterprises)
print(f'Средняя прибыль за год для всех предприятий: {glob_ave_profit}')

for ent in enterprises:
    ave_profit = ent.sum_profit
    if ave_profit > glob_ave_profit:
        result = 'выше среднего'
    elif ave_profit < glob_ave_profit:
        result = 'ниже среднего'
    else:
        result = 'равна среднему'
    print(f'Прибыль предприятия {ent.name} {result}.')
