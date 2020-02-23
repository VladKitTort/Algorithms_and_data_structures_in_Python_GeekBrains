# Во втором массиве сохранить индексы четных элементов первого массива. Например,
# если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')


indexes = []
num_index = 0
for i in array:
    if int(i) % 2 == 0:
        indexes.append(num_index)
    num_index += 1
print(f'Номера индексов четный чисел массива: {indexes}')
