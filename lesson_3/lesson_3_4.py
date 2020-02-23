# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')

num = array[0]
max_num = 1
for i in range(SIZE):
    quantity = 1
    for p in range(i + 1, SIZE):
        if array[i] == array[p]:
            quantity += 1
    if quantity > max_num:
        max_num = quantity
        num = array[i]

if max_num > 1:
    print(f'Больше всего в массиве встречается цыфра {num}, {max_num} раз.')
else:
    print('Все числа массива уникальны.')
