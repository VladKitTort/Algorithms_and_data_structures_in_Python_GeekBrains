# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20000
MIN_ITEM = -1000000
MAX_ITEM = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')

index_min_number_1 = 0
index_min_number_2 = 0

if array[0] > array[1]:
    index_min_number_2 = 1
else:
    index_min_number_1 = 1

for i in range(2, SIZE):
    if array[i] < array[index_min_number_1]:
        p = index_min_number_1
        index_min_number_1 = i
        if array[p] < array[index_min_number_2]:
            index_min_number_2 = p
    elif array[i] < array[index_min_number_2]:
        index_min_number_2 = i

print(f'Первое минимальное число в массиве: {array[index_min_number_1]}')
print(f'Второе минимальное число в массиве: {array[index_min_number_2]}')

