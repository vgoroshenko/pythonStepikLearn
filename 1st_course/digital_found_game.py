import random

congratulation_message = 'Вы угадали, поздравляем! Ваше кол-во попыток:'
enter_range_message = 'Введите диапазон чисел от 1 до '
enter_digit_message = 'Введите чило "Угадайка" от 1 до '
end_game_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
few_again_try_message = 'Слишком мало, попробуйте еще раз'
lot_again_try_message = 'Слишком много, попробуйте еще раз'
try_again_message = 'Хотите попробовать ещё раз? (Да или Нет): '
welcome_message = 'Добро пожаловать в числовую угадайку'
wrong_char_message = 'А может быть все-таки введем целое число '
yes_flag = 'д'
fail_count = []

def check_num(num):
    while True:
        if is_valid(num) == True:
            num = int(num)
            return num
        else:
            num = input(wrong_char_message)

def count_fail():
    fail_count.append(1)

def end_game():
    print(congratulation_message, sum(fail_count))
    if try_again() == True:
        start_game()
    else:
        print(end_game_message)

def is_valid(num):
    num = str(num)
    if not num.isdigit() or int(num) == 0:
        return False
    else:
        return True

def random_num(stop_range):
    return random.randint(1, stop_range)

def start_game():
    stop_range = check_num(input(enter_range_message))
    randome = random_num(int(stop_range))
    num = check_num(input(f'{enter_digit_message}{stop_range}: '))
    try_game(num, randome)
    return stop_range, num

def try_again():
    try_again = input(try_again_message)
    if yes_flag in try_again.lower():
        return True
    else:
        return False

def try_game(num, randome):
    while True:
        if int(num) > randome:
            print(lot_again_try_message)
            count_fail()
        elif int(num) < randome:
            print(few_again_try_message)
            count_fail()
        else:
            end_game()
            break
        num = input()
        num = check_num(num)

print(welcome_message)
start_game()