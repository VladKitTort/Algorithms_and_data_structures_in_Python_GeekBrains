# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

# https://drive.google.com/open?id=1iFhaFrAzWSLYvLHldWOVN8CSHM9m_9j5

n = int(input('Введите количество множеств: '))

z = 0
for i in range(n + 1):
    z += i
if z == n * (n+1)/2:
    print(True)
else:
    print(False)
