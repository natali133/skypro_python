def month_to_season(month):
    if 3 <= month <= 5:
        print("Весна")
    elif 6 <= month <= 8:
        print("Лето")
    elif 9 <= month <= 11:
        print("Осень")
    elif month == 12 or 1 <= month <= 2:
        print("Зима")


month_to_season(7)       