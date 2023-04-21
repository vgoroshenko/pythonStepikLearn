# class ebalas():
#     asd = 'ewe'
#     def wewe(self):
#         print('we')
#
# hh = ebalas().wewe
#
# print(hh)


# import json
#
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
#
# print(json.dumps(countries, separators=(',', ' - '), sort_keys=True, indent=3))

# import json
#
# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }
#
# data_json = json.dumps(words, skipkeys=True)

# import json
#
# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
#
# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
#
# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
#
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump([club1, club2, club3], f, indent=3)

# import json
#
# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }
#
# specs_json = json.dumps(specs, ensure_ascii=False, indent=3)
#
# print(specs_json)

# def is_correct_json(string):
#     try:
#         json.loads(string)
#         return True
#     except ValueError:
#         return False
#
# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
# print(is_correct_json(data))
#
# print(is_correct_json('number = 17'))


# import json, sys

# asd = [line.strip() for line in sys.stdin if '{' not in line and '}' not in line]
# asd = sys.stdin.read()
# print([asd.strip()])
# print(json.load(sys.stdin))
# [print(f'{key}: {value}') for key, value in json.load(sys.stdin)]

# import json, sys
#
#
# json_data = json.load(sys.stdin)
# for key, value in json_data.items():
#     if type(value) == list:
#         print(f'{key}: {", ".join(map(str, value))}')
#     else:
#         print(f'{key}: {value}')

import json, sys

# def test(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
#         tmp = []
#         for i in range(len(json_data)):
#             jd = json_data[i]
#             if type(jd) == bool:
#                 if jd == True:
#                     tmp.append(False)
#                 else:
#                     tmp.append(True)
#             elif type(jd) == dict:
#                 jd.update({"newkey": None})
#                 tmp.append(jd)
#             elif type(jd) == str:
#                 tmp.append(jd + '!')
#             elif type(jd) == list:
#                 tmp.append(jd * 2)
#             elif type(jd) == int:
#                 tmp.append(jd + 1)
#     with open('updated_data.json', 'w', encoding='utf-8') as f:
#         json.dump(tmp, f, indent=3)
#
# test('data.json')

# import json
#
# with open('data1.json', 'r', encoding='utf-8') as f1, open('data2.json', 'r', encoding='utf-8') as f2:
#         file1 = json.load(f1)
#         file2 = json.load(f2)
#         file1 |= file2
#         with open('data_merge.json', 'w', encoding='utf-8') as f:
#             json.dump(file1, f, indent=3)


# import json
#
# with open('people.json', 'r', encoding='utf-8') as f:
#     people = json.load(f)
#     tmp = []
#     for i in people:
#         for j in i:
#             if j not in tmp:
#                 tmp.append(j)
#     for i in people:
#         for j in tmp:
#             if j not in i:
#                 i.update({j: None})
#     with open('updated_people.json', 'w', encoding='utf-8') as out:
#         json.dump(people, out, indent=3)

# import json
#
# with open('countries.json', 'r', encoding='utf-8') as f:
#     file = json.load(f)
#     tmp_d = {}
#     for i in file:
#         tmp_d.setdefault(i["religion"], []).append(i["country"])
#     with open('religion.json', 'w', encoding='utf-8') as out:
#         json.dump(tmp_d, out, indent=3)

# import json, csv
#
# with open('playgrounds.csv', 'r', encoding='utf-8') as f:
#     with open('addresses.json', 'w', encoding='utf-8') as out:
#         file = list(csv.reader(f, delimiter=';'))
#         tmp = {}
#         for line in file[1:]:
#             tmp.setdefault(line[1], {}).setdefault(line[2], []).append(line[3])
#         json.dump(tmp, out, indent=3, ensure_ascii=False)

# import json, csv
#
# with open('students.json', 'r', encoding='utf-8') as f:
#     with open('data.csv', 'w', encoding='utf-8', newline='') as out:
#         file = json.load(f)
#         file = sorted(file, key=lambda x: x['name'])
#         writer = csv.writer(out)
#         writer.writerow(['name', 'phone'])
#         [writer.writerow([i['name'], i['phone']]) for i in file if i['age'] >= 18 and i['progress'] >= 75]

# import json
#
# with open('pools.json', 'r', encoding='utf-8') as f:
#     file = json.load(f)
#     file = list(filter(lambda x: int(x['WorkingHoursSummer']['Понедельник'][:2]) <= 10 and int(x['WorkingHoursSummer']['Понедельник'][6:8]) >= 12, file))
#     file = sorted(sorted(file, key=lambda x: x['DimensionsSummer']['Width'], reverse=True), key=lambda x: x['DimensionsSummer']['Length'], reverse=True)
#     print(f"{file[0]['DimensionsSummer']['Length']}x{file[0]['DimensionsSummer']['Width']}", file[0]['Address'], sep='\n')

# import json,csv
#
# with open('exam_results.csv', 'r', encoding='utf-8') as fcsv:
#     with open('best_scores.json', 'w', encoding='utf-8') as fjson:
#         new_lst = []
#         fcsv = list(csv.DictReader(fcsv))
#         fcsv = sorted(fcsv, key=lambda x: x['email'])
#         #fcsv = max(fcsv, key=lambda x: int(x['best_score']))
#         fcsv = list(filter(max(fcsv, key=lambda x: x['best_score']), fcsv))
#         # for i in fcsv:
#         #     if i in new_lst:
#
#         json.dump(fcsv, fjson, indent=4)

# import json
#
# with open('food_services.json', 'r', encoding='utf-8') as f:
#     file = json.load(f)
#     tmp, tmp1 = {}, {}
#     for i in file:
#         tmp.setdefault(i['District'], []).append(i)
#         if i['OperatingCompany']:
#             tmp1.setdefault(i['OperatingCompany'], []).append(i)
#     tmp_max = max(tmp, key=lambda x: len(tmp[x]))
#     print(tmp_max, len(tmp[tmp_max]), sep=': ')
#     tmp1_max = max(tmp1, key=lambda x: len(tmp1[x]))
#     print(tmp1_max, len(tmp1[tmp1_max]), sep=': ')



import json

with open('food_services.json', 'r', encoding='utf-8') as f:
    file = json.load(f)
    tmp = {}
    for i in file:
        tmp.setdefault(i['TypeObject'], []).append(i)
    for i in sorted(tmp):
        max_count = max(tmp[i], key=lambda x: x['SeatsCount'])['SeatsCount']
        max_count_name = max(tmp[i], key=lambda x: x['SeatsCount'])['Name']
        print(i, f'{max_count_name}, {max_count}', sep=': ')


