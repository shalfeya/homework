per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада"))
a = per_cent["ТКБ"]*money/100
b = per_cent["СКБ"]*money/100
c = per_cent["ВТБ"]*money/100
d = per_cent["СБЕР"]*money/100
dep = [a, b, c, d]
deposit = max(dep)
print("Максимальная сумма, которую вы можете заработать - ", deposit)