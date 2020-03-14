import collections


def average_profit_companies(n):
    list_of_companies = collections.OrderedDict()
    total_profit = 0
    for i in range(n):
        name_companies = input(f"Введите наименование компании номер {i + 1}: ")
        profit_for_the_year = 0
        for p in range(4):
            profit_for_the_quarter = float(
                input(f"Введите прибль компании {name_companies} за {p +1} квартал 2019 года: "))
            profit_for_the_year += profit_for_the_quarter
        list_of_companies[name_companies] = profit_for_the_year
        total_profit += profit_for_the_year
    average_profit = total_profit / n
    roster_1 = collections.deque()
    roster_2 = collections.deque()
    for k in list_of_companies.keys():
        if list_of_companies.get(k) >= average_profit:
            roster_1.append(k)
        else:
            roster_2.append(k)
    print(f"\n\nСредняя прибль всех представленных фирм за прошлый год: {average_profit}"
          f"\nФирмы с прибылью равной и выше среднего значения за прошлый год: {[i for i in roster_1]}\n"
          f"Фирмы сс прибылью ниже среднего значения за прошлый год: {[i for i in roster_2]}")


average_profit_companies(int(input("Введите количество фирм, для расчета средней прибыли за прошлый год: ")))

