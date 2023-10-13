# Визначте, проектів якого жанру було найбільше випущено на Netflix у 2023році.
import pandas as pd

# Імпорт бібліотеки pandas і завантаження даних з CSV-файлу 'netflix_titles.csv' у DataFrame 'df'.
df = pd.read_csv('netflix_titles.csv')

# Вибір фільмів, які були випущені у 2021 році і збереження їх у DataFrame 'film_year'.
film_year = df[df['release_year'] == 2021]

# Обчислення кількості фільмів та серіалів за жанрами (в стовпці 'listed_in') і збереження цих значень у зміній 'release'.
release = film_year['listed_in'].value_counts()

# Вибірка перших 10 рядків результату і збереження їх у зміній 'release1'.
release1 = release.head(10)

# Виведення результатів на екран.
print(release1)
