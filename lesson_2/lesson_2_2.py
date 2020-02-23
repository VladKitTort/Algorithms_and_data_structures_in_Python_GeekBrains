# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/open?id=1iFhaFrAzWSLYvLHldWOVN8CSHM9m_9j5

num = int(input('Ведите число: '))
even = 0
uneven = 0
if num < 0:
    num *= -1
while num > 0:
    x = num % 10
    if x % 2 > 0:
        even += 1
    else:
        uneven += 1
    num //= 10
print(f'Четных чисел: {even}')
print(f'Не четных чисел: {uneven}')