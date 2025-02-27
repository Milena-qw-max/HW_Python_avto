def is_year_leap(n):
    return n % 4 == 0


year = int(input('Введите год:'))
i = is_year_leap(year)

print(f'год {year}: {i}')
