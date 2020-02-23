# https://drive.google.com/open?id=1eeKgHgP5Y6dd1RygSDY8ZyP2MhPQLoMs
print('Введите длину отрезков треугольника ABC.')
ab = float(input('\tAB = '))
bc = float(input('\tBC = '))
ca = float(input('\tCA = '))
if ab + bc > ca and bc + ca > ab and ca + ab > bc:
    if ab == bc == ca:
        print('Треугольник равносторонний.')
    elif ab == bc or bc == ca or ca == ab:
        print('Треугольник равнобедренный.')
    else:
        print('Треугольник разносторонний.')
else:
    print('Треугольник с такими сторонами построить не возможно.')