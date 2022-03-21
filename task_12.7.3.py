money = float(input("Введите сумму вклада"))
money /= 100
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = float(per_cent['ТКБ'] * money)
b = float(per_cent['СКБ'] * money)
c = float(per_cent['ВТБ'] * money)
d = float(per_cent['СБЕР'] * money)
deposit = [a, b, c, d]
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max_deposit)
