# from collections import ChainMap
#
# with open('zoo.json', 'r', encoding='utf-8') as f:
#     file = sum(ChainMap(*json.load(f)).values())
# print(file)

from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingridients = ChainMap(bread, meat, sauce, vegetables, toppings)

check = Counter(input().split(','))
total = sum(ingridients[k] * v for k, v in check.items())

max_len = len(max(check, key=len))
[print(f'{key}{(max_len - len(key)) * " "} x {value}') for key, value in sorted(check.items())]

tmp_total = len(f'ИТОГ: {total}р')
tmp_len = max_len + len(f' x {max(check.values())}')

print('-' * max([tmp_len, tmp_total]), f'ИТОГ: {total}р', sep='\n')