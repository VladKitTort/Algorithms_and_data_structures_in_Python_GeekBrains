# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#

import timeit
import cProfile

# 1 Вариант. Функция линейна.


def op_1(n):
    res = []
    p = int(n * 10)
    while n > len(res):
        sieve_1 = [i for i in range(p)]
        sieve_1[1] = 0
        for i in range(2, p):
            if sieve_1[i] != 0:
                j = i + i
                while j < p:
                    sieve_1[j] = 0
                    j += i
        res = [i for i in sieve_1 if i != 0]
        p = int(p * 1.3)
    return res[n - 1]


print(timeit.timeit('op_1(100)', number=100, globals=globals()))  # 0.055741
print(timeit.timeit('op_1(300)', number=100, globals=globals()))  # 0.177728
print(timeit.timeit('op_1(900)', number=100, globals=globals()))  # 0.5602187999999999
print(timeit.timeit('op_1(1200)', number=100, globals=globals()))  # 0.7268668
print(timeit.timeit('op_1(3600)', number=100, globals=globals()))  # 2.1101974


cProfile.run('op_1(900)')  # 1    0.004    0.004    0.005    0.005 lesson_4_2_1.py:5(sieve)
cProfile.run('op_1(1200)')  # 1    0.006    0.006    0.007    0.007 lesson_4_2_1.py:5(sieve)
cProfile.run('op_1(3600)')  # 1    0.015    0.015    0.019    0.019 lesson_4_2_1.py:5(sieve)

# 2 Вариант. Квадратичная функция.


def op_2(n):
    sieve_1 = [i for i in range(n * 15)]
    for i in range(2):
        del sieve_1[0]
    sieve_2 = []
    for i in sieve_1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            sieve_2.append(i)
    return sieve_2[n - 1]


print(timeit.timeit('op_2(100)', number=100, globals=globals()))  # 1.7420434999999999
print(timeit.timeit('op_2(200)', number=100, globals=globals()))  # 6.3726475
print(timeit.timeit('op_2(400)', number=100, globals=globals()))  # 23.954792999999995
print(timeit.timeit('op_2(600)', number=100, globals=globals()))  # 51.552808899999995
print(timeit.timeit('op_2(800)', number=100, globals=globals()))  # 89.60953310000001


cProfile.run('op_2(400)')  # 1    0.002    0.002    0.002    0.002 lesson_4_2_1.py:29(op)
cProfile.run('op_2(600)')  # 1    0.004    0.004    0.004    0.004 lesson_4_2_1.py:29(op)
cProfile.run('op_2(800)')  # 1    0.006    0.006    0.006    0.006 lesson_4_2_1.py:29(op)

print(op_1(200))
print(op_2(220))