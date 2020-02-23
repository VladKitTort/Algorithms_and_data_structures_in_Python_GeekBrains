# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


RANGE_MIN = 2
RANGE_MAX = 99
MULTIPLE_MIN = 2
MULTIPLE_MAX = 9


for i in range(MULTIPLE_MIN, MULTIPLE_MAX + 1):
    counter = 0
    for n in range(RANGE_MIN, RANGE_MAX + 1):
        if n % i == 0:
            counter += 1
    print(f'В диапазоне от {RANGE_MIN} до {RANGE_MAX} цыфра {i} будет делителем для {counter} чисел.')