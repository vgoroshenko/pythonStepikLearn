import random

variants = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

hello_message = 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.'
name_question_message = 'Как тебя зовут? '
hello_name_message = 'Привет '
say_question_message = 'Что ты хочешь узнать? '
second_question_message = 'Хочешь узнать что то ещё? (да или нет): '
returne_message = 'Возвращайся если возникнут вопросы!'
fail_flag = 'д'

print(hello_message)
print(hello_name_message, input(name_question_message))
while True:
    input(say_question_message)
    print(random.choice(variants))
    second_question = input(second_question_message)
    if fail_flag in second_question:
        continue
    else:
        print(returne_message)
        break
