# https://drive.google.com/open?id=1BihdPa5hecSoSHpB3EoSh4XZU_GcGMLS
print('Введите год для определения, високосный он или нет: ')
year = int(input())
if year % 4 == 0:
    print(f'Год {year} високосный.')
else:
    print(f'Год {year} не високосный.')