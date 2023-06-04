# from functools import partial
#
# to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
#
# send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')

import sys
from functools import lru_cache

@lru_cache
def sort_chars(word):
    return ''.join(sorted(word.strip()))

[print(sort_chars(i)) for i in sys.stdin]