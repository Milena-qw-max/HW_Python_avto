def month_to_season(n):
    if 0 < n < 3 or n == 12:
        return 'Зима'
    elif 2 < n < 6:
        return 'Весна'
    elif 5 < n < 9:
        return 'Лето'
    elif 8 < n < 12:
        return 'Осень'
    else:
        return "Введите число от 1 до 12"


print(month_to_season(26))
