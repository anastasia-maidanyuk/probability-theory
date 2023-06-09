import math
import numpy as np
import pandas as pd
import scipy
from scipy.stats import norm
from tabulate import tabulate

# ЛАБОРАТОРНА РОБОТА No2.
# Варіант 55
mu = 5  # математичне сподівання
sigma = 1.8  # стандартне відхилення
size = 144  # кількість чисел

# Завдання 1
def task1():
    our_array = get_output_array(5, 1.8, 144)
    print("Завдання 1")
    print("Масив даних")
    print(str(our_array))
    print("Інтервал для 95%:")
    interval_output(our_array, 0.95, True)

# Завдання 2
def task2():
    print("Завдання 2")
    array_sizes = list(range(125, 5, -5))
    percentages = [0.99]
    results_data = []

    for array_size in array_sizes:
        for percent in percentages:
            array = get_output_array(5, 1.8, array_size)
            result = interval_output(array, percent, False)
            lower_u = round(result.get("down_border_interval"), 5)
            upper_u = round(result.get("up_border_interval"), 5)
            lower_sigma = round(result.get("down_sigma"), 5)
            upper_sigma = round(result.get("up_sigma"), 5)
            data = {
                'Розмір': array_size,
                'Відсоток': str(percent * 100) + '%',
                'Математичне сподівання': f'{lower_u} < u < {upper_u}',
                'Середньоквадратичне відхилення': f'{lower_sigma} < σ < {upper_sigma}'
            }
            results_data.append(data)

    df = pd.DataFrame(results_data)
    df = df.set_index('Розмір')
    print(tabulate(df, headers='keys', tablefmt='pretty'))


from scipy.stats import norm, chi2


def interval_output(array, percent, print_values):
    not_x = np.mean(array)
    n = len(array)
    s = np.std(array, ddof=1)
    t = abs(norm.ppf((1 - percent) / 2, loc=0, scale=1))
    down_sigma = (n - 1) * (s ** 2) / chi2.ppf(1 - (1 - percent) / 2, n - 1)
    up_sigma = (n - 1) * (s ** 2) / chi2.ppf((1 - percent) / 2, n - 1)
    down_border_interval = not_x - (t * s / np.sqrt(n))
    up_border_interval = not_x + (t * s / np.sqrt(n))

    result = {'down_border_interval': down_border_interval, 'up_border_interval': up_border_interval,
              'down_sigma': down_sigma, 'up_sigma': up_sigma}

    if print_values:
        print(f"Вибіркове середнє значення вибірки: {not_x}")
        print(f"Кількість елементів: {n}")
        print(f"Середнье відхилення: {s:.3f}")
        print(f"Критичне значення: {t:.3f}")
        print(f"Нижня межа інтервалу: {down_border_interval:.3f}")
        print(f"Верхня межа інтервалу: {up_border_interval:.3f}")
        print(f"Загальний вигляд: {down_border_interval:.4f} < u < {up_border_interval:.4f}")
        print(f"Cередньоквадратичне відхилення: {down_sigma:.4f} < σ < {up_sigma:.4f}")

    return result

def get_output_array(mean, variance, size):
    np.random.seed(0)
    return np.random.normal(loc=mean, scale=np.sqrt(variance), size=size)


task1()
task2()
