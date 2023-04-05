import random

first_group = ['Трусова', 'Смирнов', 'Волкова', 'Богданова', 'Николаев', 'Шишмарёва', 'Журавлёв', 'Веселова', 'Ковалёв',
               'Шевцова']
second_group = ['Иванов', 'Панин', 'Полко', 'Ливонская', 'Морозов', 'Трошина', 'Кузнецова', 'Родионов', 'Яковлева',
                'Беляев']
team = tuple(random.sample(first_group, 5) + random.sample(second_group, 5))
print(first_group)
print(second_group)
print(team)
print('длина кортежа:', len(team))
team = tuple(sorted(team))
if 'Иванов' in team:
    print(team.count('Иванов'))
else:
    print('Иванова нет')
