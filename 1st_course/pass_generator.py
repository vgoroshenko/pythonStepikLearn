import random
from string import *

pass_count_message = 'Введите количество паролей для генерации: '
len_pass_message = 'Введите длинну одного пароля (от 8): '
digit_count_message = 'Включать ли цифры (д/н): '
uppercase_count_message = 'Включать ли прописные буквы (д/н): '
lowercase_count_message = 'Включать ли строчные буквы (д/н): '
punctuation_count_message = 'Включать ли символы (д/н): '
yes_flag = ['д', 'Д', 'y', 'Y', '']

chars_list =['']

def question():
    pass_count = int(input(pass_count_message))
    len_pass = int(input(len_pass_message))
    if input(digit_count_message) in yes_flag:
        chars_list.extend(digits)
    if input(uppercase_count_message) in yes_flag:
        chars_list.extend(ascii_uppercase)
    if input(lowercase_count_message) in yes_flag:
        chars_list.extend(ascii_lowercase)
    if input(punctuation_count_message) in yes_flag:
        chars_list.extend(punctuation)
    print()
    return pass_count, len_pass


def generate_password(len_pass, chars):
    passwd = ''
    for i in range(len_pass):
        passwd += random.choice(chars)
    return passwd

def start_passwd_gen():
    pass_count, len_pass = question()
    for _ in range(1, pass_count + 1):
        print(f'Пароль #{_}: ', generate_password(len_pass, ''.join(chars_list)))

start_passwd_gen()