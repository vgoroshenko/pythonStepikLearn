# from collections import Counter
#
# counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# counter2 = Counter(s=4, i=4, p=2, m=1)
# counter3 = Counter('iiiisspm')
#
# print(counter1 == counter2)
# print(counter1 == counter3)

# from collections import Counter
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# [print(f'{key}: {value}') for key, value in sorted(Counter([i.split('.')[1] for i in files]).items())]


# from collections import Counter
# def count_occurences(word, words):
#     return Counter([i.lower() for i in words.split()])[word.lower()]
#
# word = 'Se'
# words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'
#
# print(count_occurences(word, words))

# from collections import Counter
#
# [print(f'{key}: {value}') for key, value in sorted(Counter(input().split(',')).items())]

# from collections import Counter
#
# fruit_list = input().split(',')
#
# [print(f'{key}{(max(map(lambda x: len(x), fruit_list)) - len(key)) * " "}: {sum([ord(i) for i in key if i != " "])}\
#  UC x {value} = {sum([ord(i) for i in key if i != " "]) * value} UC') \
#  for key, value in sorted(Counter(fruit_list).items())]


from collections import Counter
import string

with open('pythonzen.txt', 'r', encoding='utf-8') as f:
    char_count = Counter(list(f.read().lower()))
    [print(f'{key}: {value}') for key, value in sorted(char_count.items()) if key in string.ascii_letters]
