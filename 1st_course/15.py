# import random
#
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
#
# print(num1)
# print(num2)

# import random
#
# def random_num():
#     return random.randint(1, 100)
#
# num = int(input())
# randome = random_num()
#
# while True:
#     if num > randome:
#         print('Слишком много, попробуйте еще раз')
#     elif num < randome:
#         print('Слишком мало, попробуйте еще раз')
#     else:
#         print('Вы угадали, поздравляем!')
#         break
#     num = int(input())


# import math
# num = int(input())
# print(math.ceil(math.log2(num)))


# import random
#
# _welcome_message = 'Добро пожаловать в числовую угадайку'
# bye_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
#
# start_range = 1
# stop_range = 100
#
# fail_count = 0
#
#
# def random_num():
#     return random.randint(start_range, stop_range)
#
# def is_valid(num):
#     if not num.isdigit() or int(num) > stop_range or int(num) == 0:
#         return False
#     else:
#         return True
#
# def check_num(num):
#     while True:
#         if is_valid(num) == True:
#             num = int(num)
#             return num
#         else:
#             num = input('А может быть все-таки введем целое число от 1 до 100?')
#
# def welcome_message():
#     print(_welcome_message)
#
#
# welcome_message()
# randome = random_num()
#
# num = input('Введите чило от 1 до 100:')
#
# num = check_num(num)
# while True:
#     if int(num) > randome:
#         print('Слишком много, попробуйте еще раз')
#     elif int(num) < randome:
#         print('Слишком мало, попробуйте еще раз')
#     else:
#         print('Вы угадали, поздравляем!')
#         break
#     num = input()
#     fail_count += 1
#     num = check_num(num)
#
#
# print('Спасибо, что играли в числовую угадайку. Еще увидимся...')



import random


welcome_message = 'Добро пожаловать в числовую угадайку'
congratulation_message = 'Вы угадали, поздравляем!'
wrong_char_message = 'А может быть все-таки введем целое число '
lot_again_try_message = 'Слишком много, попробуйте еще раз'
few_again_try_message = 'Слишком мало, попробуйте еще раз'
try_again_message = 'Хотите попробовать ещё раз? '
yes_flag = 'д'
end_game_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'

def random_num(start_range, stop_range):
    if start_range == '':
        start_range = 1
        stop_range = 100
    return random.randint(start_range, stop_range)

def is_valid(num, start_range, stop_range):
    if not num.isdigit() or int(num) > int(stop_range) or int(num) == 0:
        return False
    else:
        return True

def welcome_game():
    start_range = input('Введите диапазон чисел от ')
    stop_range = input('до ')
    randome = random_num(int(start_range), int(stop_range))
    num = input(f'Введите чило "Угадайка" от {start_range} до {stop_range}:')
    return start_range, stop_range, randome, num

def check_num(num):
    while True:
        if is_valid(num, start_range, stop_range) == True:
            num = int(num)
            return num
        else:
            num = input(wrong_char_message)

def try_game(num):
    num = check_num(num)
    while True:
        if int(num) > randome:
            print(lot_again_try_message)
        elif int(num) < randome:
            print(few_again_try_message)
        else:
            end_game()
            break
        num = input()
        num = check_num(num)

def end_game():
    print(congratulation_message)
    if try_again() == True:
        welcome_game()
    else:
        print(end_game_message)

def try_again():
    try_again = input(try_again_message)
    if yes_flag in try_again.lower():
        return True
    else:
        return False


print(welcome_message)
start_range, stop_range, randome, num = welcome_game()
try_game(num)


