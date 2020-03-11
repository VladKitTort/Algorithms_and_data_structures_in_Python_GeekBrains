# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
# задания первых трех уроков.
# Проверка равенства: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# По данным проверки можно сделать вывод, что наиболее быстрый споособ для проверки равенства показала функция Второго
# варианта.


import timeit
import cProfile


# 1 Вариант. Функция линейна.

def fan_1(n):
    if n == 1:
        return n
    sum_n = n + fan_1(n - 1)
    return sum_n


print(timeit.timeit('fan_1(100)', number=100, globals=globals()))  # 0.003788899999999998
print(timeit.timeit('fan_1(300)', number=100, globals=globals()))  # 0.010654500000000004
print(timeit.timeit('fan_1(500)', number=100, globals=globals()))  # 0.020349199999999998
print(timeit.timeit('fan_1(700)', number=100, globals=globals()))  # 0.02556109999999999
print(timeit.timeit('fan_1(900)', number=100, globals=globals()))  # 0.0350689


cProfile.run('fan_1(500)')  # 500/1    0.000    0.000    0.000    0.000 lesson_4_1.py:10(fan)
cProfile.run('fan_1(700)')  # 700/1    0.001    0.000    0.001    0.001 lesson_4_1.py:10(fan)
cProfile.run('fan_1(900)')  # 900/1    0.001    0.000    0.001    0.001 lesson_4_1.py:10(fan)


# 2 Вариант. Функция линейна.

def fan_2(n):
    z = 0
    for i in range(n + 1):
        z += i
    if z == n * (n + 1) / 2:
        return True
    else:
        return False


print(timeit.timeit('fan_2(100)', number=100, globals=globals()))  # 0.0011363000000000067
print(timeit.timeit('fan_2(300)', number=100, globals=globals()))  # 0.0024877999999999845
print(timeit.timeit('fan_2(500)', number=100, globals=globals()))  # 0.004189300000000007
print(timeit.timeit('fan_2(700)', number=100, globals=globals()))  # 0.006622900000000015
print(timeit.timeit('fan_2(900)', number=100, globals=globals()))  # 0.008298699999999992


cProfile.run('fan_2(10000)')  # 1    0.001    0.001    0.001    0.001 lesson_4_1.py:30(fan_2)
cProfile.run('fan_2(100000)')  # 1    0.011    0.011    0.011    0.011 lesson_4_1.py:30(fan_2)
cProfile.run('fan_2(1000000)')  # 1    0.104    0.104    0.104    0.104 lesson_4_1.py:30(fan_2)


# 3 Вариант. Функция линейна.


def fan_3(n):
    if n > 2:
        p = list(range(0, n + 1))
        s = 1
        z = 0
        a = len(p)
        while a > 1:
            z = z + p[s]
            s += 1
            a -= 1
        if z == n * (n + 1) / 2:
            return True
        else:
            return False
    else:
        return n


print(timeit.timeit('fan_3(10)', number=100, globals=globals()))  # 0.0004047000000000009
print(timeit.timeit('fan_3(100)', number=100, globals=globals()))  # 0.0029547000000000045
print(timeit.timeit('fan_3(1000)', number=100, globals=globals()))  # 0.0331982
print(timeit.timeit('fan_3(10000)', number=100, globals=globals()))  # 0.3549203
print(timeit.timeit('fan_3(100000)', number=100, globals=globals()))  # 3.4415435

cProfile.run('fan_3(1000)')  # 1    0.000    0.000    0.000    0.000 1.py:5(fan_3)
cProfile.run('fan_3(10000)')  # 1    0.003    0.003    0.003    0.003 1.py:5(fan_3)
cProfile.run('fan_3(100000)')  # 1    0.030    0.030    0.030    0.030 1.py:5(fan_3)
