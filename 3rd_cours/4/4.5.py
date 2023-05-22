# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     print(len(zip_file.infolist()))
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)
#     print(len(zip_file.namelist()))


# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     print(len([i for i in zip_file.namelist() if '.' in i]))


# from zipfile import ZipFile
# from functools import reduce
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     print(f'Объем исходных файлов: {reduce(lambda x, y: x + y.file_size, info, 0)} байт(а)')
#     print(f'Объем сжатых файлов: {reduce(lambda x, y: x + y.compress_size, info, 0)} байт(а)')

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     tmp = {i.filename.split('/')[-1]: (i.compress_size / i.file_size) * 100 for i in info if not i.is_dir()}
#     print(min(tmp, key=lambda x: tmp[x]))


# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     print(*sorted([i.filename.split('/')[-1] for i in info if not i.is_dir() \
#                    and datetime(*i.date_time) > datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')]), sep='\n')


# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     tmp = {i.filename.split('/')[-1]:[i.date_time, i.file_size, i.compress_size] for i in info if not i.is_dir()}
#     for key, value in sorted(tmp.items()):
#         print(key,
#               f'  Дата модификации файла: {datetime(*value[0])}',
#               f'  Объем исходного файла: {value[1]} байт(а)',
#               f'  Объем сжатого файла: {value[2]} байт(а)', sep='\n', end='\n\n')


# from zipfile import ZipFile
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     for i in file_names:
#         zip_file.write(i)

# from zipfile import ZipFile
# import os
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# with ZipFile('files.zip', mode='a') as zip_file:
#     for i in file_names:
#         with open(i, 'rb') as file:
#             if len(file.read()) < 100:
#                 zip_file.write(i)
# #         if os.path.getsize(i) < 100:
# #             zip_file.write(i)


# from zipfile import ZipFile
#
# def extract_this(zip_name, *args):
#     with ZipFile(zip_name) as zip_file:
#         [zip_file.extract(i.filename) for i in zip_file.infolist() if i.filename.split('/')[-1] in args] if args else zip_file.extractall()
#
# extract_this('workbook.zip', 'earth.jpg', 'exam.txt', 'qwe.ww')


# from zipfile import ZipFile
# import json
#
# def is_correct_json(string):
#     try:
#         json.loads(string)
#         return True
#     except ValueError:
#         return False
#
# with ZipFile('data.zip') as zf:
#     qq = [zf.read(i).decode('latin-1') for i in zf.namelist()
#           if '.json' in i.split('/')[-1]
#           and is_correct_json(zf.read(i).decode('latin-1'))
#           and 'Arsenal' in zf.read(i).decode('latin-1')]
#
#     for i in sorted(qq):
#         tmp_json = json.loads(i)
#         print(tmp_json['first_name'], tmp_json['last_name'], sep=' ')


# from zipfile import ZipFile
#
# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1000:
#         return f'{size} B'
#     elif 1000 <= size < 1000000:
#         return f'{round(size / 1024)} KB'
#     elif 1000000 <= size < 1000000000:
#         return f'{round(size / 1048576)} MB'
#     else:
#         return f'{round(size / 1073741824)} GB'
#
# with ZipFile('test.zip') as zf:
#     tmp = []
#     for i in zf.infolist():
#         if not i.is_dir():
#             tmp.append(i.filename.split('/'))
#     print(tmp)
            # for j in i.filename.split('/'):
            #     if j != i.filename.split('/'):
            #         print(j, end='\n  ')
            #     else:
            #         print(j, i.file_size)



















