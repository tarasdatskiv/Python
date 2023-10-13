# Фільми на Netflix частіше виходять весною чи восени? А серіали?
import pandas as pd

# Ініціалізація змінних для підрахунку фільмів весною та осінню.
vesna = 0
osin = 0

# Створення словника 'monthCounter' з ключами - назвами місяців і початковими значеннями 0 для кожного місяця.
monthCounter = {"January": 0,
                "February": 0,
                "March": 0,
                "April": 0,
                "May": 0,
                "June": 0,
                "July": 0,
                "August": 0,
                "September": 0,
                "October": 0,
                "November": 0,
                "December": 0}

# Завантаження даних з CSV-файлу 'netflix_titles.csv' у DataFrame 'data' за допомогою бібліотеки pandas.
data = pd.read_csv("netflix_titles.csv")

# Цикл для обходу кожного рядка у DataFrame 'data'.
for i in range(len(data)):
    row = data.loc[i]
    date = row["date_added"]

    # Перевірка, чи поле 'date_added' має тип str.
    if type(date) != str:
        continue

    # Перевірка типу контенту (фільм чи серіал) та підрахунок фільмів за місяцем додавання.
    if row['type'] == "Movie":
        for monthCheck in monthCounter.keys():
            if monthCheck in date:
                monthCounter[monthCheck] += 1

# Підрахунок кількості фільмів, які були додані весною та осінню.
for month, value in monthCounter.items():
    if month == "March" or month == "April" or month == "May":
        vesna += value
    elif month == "September" or month == "October" or month == "November":
        osin += value

# Виведення результату на екран.
print(f'Весною {vesna} фільмів\nВосени {osin} фільмів')