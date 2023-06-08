import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# ЛАБОРАТОРНА РОБОТА No1. ОПИСОВА СТАТИСТИКА
# Варіант 55
mu = 5  # математичне сподівання
sigma = 1.8  # стандартне відхилення
size = 144  # кількість чисел
xy = [4, 4, 3, 7, 7, 1, 2, 7, 2, 9, 4, 5, 3, 6, 5, 2, 5, 1, 8, 4, 3, 5, 3, 3, 7, 7, 7, 5, 7, 6, 4, 1, 1, 8, 5, 5, 4, 2,
      5, 3, 5, 7, 7, 6, 6, 5, 6, 4, 6, 9, 6, 4, 5, 3, 1, 7, 9, 2, 6, 6, 3, 5, 6, 4, 4, 4, 3, 3, 3, 5, 10, 7, 3, 5, 4, 4,
      4, 9, 3, 5, 2, 5, 3, 6, 4, 6, 2, 3, 5, 9, 8, 3, 6, 3, 5, 4, 6, 6, 5, 2, 6, 4, 7, 5, 5, 5, 6, 5, 9, 6, 2, 4, 7, 3,
      2, 6, 1, 4, 3, 6, 5, 5, 6, 1, 8, 5, 2, 2, 4, 3, 6, 1, 4, 7, 4, 3, 5, 4, 2, 4, 5, 6, 3, 3]  # генеруємо


# --------------РОЗРАХУНКИ-----------------
# Вибіркове середнє
def average(xy):
    return sum(xy) / len(xy)


# Медіану
def mediana(xy):
    sorted_xy = sorted(xy)
    n = len(sorted_xy)
    if n % 2 == 0:
        # парна(повертаємо середнє значення двох серединних елементів)
        return (sorted_xy[n // 2 - 1] + sorted_xy[n // 2]) / 2
    else:
        # непарна(повертаємо серединний елемент)
        return sorted_xy[n // 2]


# Моду
def moda(xy):
    count = {}
    for x in xy:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    max_count = max(count.values())
    modas = [num for num, v in count.items() if v == max_count]
    return modas[0]


# Дисперсію
def calculate_variance(xy):
    n = len(xy)
    xy_average = sum(xy)
    variance = sum((x - xy_average) ** 2 for x in xy) / (n - 1)
    return variance


# Середньоквадратичне відхилення заданої вибірки
def standard_deviation(xy):
    n = len(xy)
    xy_average = sum(xy) / n
    variance = sum((x - xy_average) ** 2 for x in xy) / (n - 1)
    std_deviation = math.sqrt(variance)
    return std_deviation


# Виводимо результати
print(f"Вибіркове середнє: {average(xy)}")
print(f"Медіана: {mediana(xy)}")
print(f"Мода: {moda(xy)}")
print(f"Вибіркова дисперсія: {calculate_variance(xy)}")
print(f"Середньоквадратичне відхилення: {standard_deviation(xy)}")


# --------------ДІАГРАМИ-----------------
# Графік
plt.figure(figsize=(18, 12))


# Полігон частот
plt.subplot(231)
sns.kdeplot(xy, color='pink')
plt.title('Полігон частот')


# Гістограму частот
plt.subplot(232)
plt.hist(xy, bins='auto', color='lightblue', alpha=0.83, rwidth=0.76)
plt.title('Гістограма частот')


# Діаграми розмаху
plt.subplot(234)
sns.boxplot(xy, color='turquoise')
plt.title('Діаграма розмаху')


# Кругова
plt.subplot(235)
bins = pd.cut(xy, bins=10)
labels, counts = np.unique(bins, return_counts=True)
plt.pie(counts, labels=labels, colors=sns.color_palette("pastel"))
plt.title('Кругова діаграма')


# Парето
plt.subplot(236)
counts = bins.value_counts().sort_values(ascending=False)
counts.plot(kind='bar', color='orange')
plt.title('Діаграма Парето')


plt.tight_layout()
plt.show()
