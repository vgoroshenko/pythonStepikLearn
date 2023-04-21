# chars = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# move_on = int(input())
# text = input()
# for i in range(len(text)):
#     num_char = ord(text[i])
#     if num_char - move_on < 97:
#         char = num_char - move_on
#         total_char = 97 - (char + 1)
#         total = ord(chr(122)) - total_char
#         print(chr(total), end='')
#     else:
#         print(chr(ord(text[i]) - move_on), end='')
#
chars = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
move_on = int(input())
text = input()
for i in range(len(text)):
    num_char = ord(text[i])
    if num_char - move_on < 97:
        char = num_char - move_on
        total_char = 97 - (char + 1)
        total = ord(chr(122)) - total_char
        print(chr(total), end='')
    else:
        print(chr(ord(text[i]) - move_on), end='')