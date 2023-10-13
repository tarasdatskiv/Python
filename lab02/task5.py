# В якому році на Netflix було випущено найбільшу кількість фільмів?
import pandas

# Імпорт бібліотеки pandas.
df = pandas.read_csv('netflix_titles.csv')
# Завантаження даних з CSV-файлу 'netflix_titles.csv' у DataFrame 'df'.

# Вибір фільмів (записів з типом 'Movie') з DataFrame 'df' і зберігання їх у зміній 'film_year'.
film_year = df[(df['type'] == 'Movie')]

# Обчислення кількості фільмів для кожного року випуску і зберігання цих значень у зміній 'relise'.
release = film_year['release_year'].value_counts()

# Вибірка року з найбільшою кількістю випущених фільмів і зберігання цієї інформації у зміній 'top1'.
top1 = release.head(5)

# Виведення результату (року з найбільшою кількістю фільмів) на екран.
print(top1)