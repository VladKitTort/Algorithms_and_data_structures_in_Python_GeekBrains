# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 200
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')

num_min = array[0]
num_max = array[0]

for i in array:
    if num_min >= i:
        num_min = i
    if num_max <= i:
        num_max = i

index_min = array.index(num_min)
index_max = array.index(num_max)

sum_num = 0
if index_min < index_max:
    for i in array[(index_min + 1): index_max]:
        sum_num += i
else:
    for i in array[(index_max + 1): index_min]:
        sum_num += i
print(f'Сумма всех чисел между {num_min} и {num_max}: {sum_num}')