# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/open?id=1iFhaFrAzWSLYvLHldWOVN8CSHM9m_9j5

n = int(input())

z = 1
k = 1
for i in range(n):
    z = (z / 2) * (-1)
    k = k + z

print(f'Итоговая сумма чисел: {k}')


