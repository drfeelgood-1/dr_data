"""Модуль game_core_v3 — решение задания «Угадай число».

Содержит три алгоритма угадывания числа от 1 до 100 и функцию
тестирования score_game, вычисляющую среднее число попыток
на 10000 случайных загаданных чисел.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию
    о больше или меньше. Функция принимает загаданное число
    и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count


def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше
    нужного. Функция принимает загаданное число и возвращает
    число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count


def game_core_v3(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска.
    На каждом шаге диапазон возможных значений делится пополам,
    что гарантирует нахождение числа за не более чем log2(100) ~ 7
    попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100
    while True:
        count += 1
        predict = (low + high) // 2
        if number == predict:
            break
        elif number > predict:
            low = predict + 1
        else:
            high = predict - 1
    return count


def score_game(core_function) -> int:
    """За какое количество попыток в среднем за 10000 подходов
    угадывает наш алгоритм.

    Args:
        core_function (callable): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))
    for number in random_array:
        count_ls.append(core_function(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score


if __name__ == '__main__':
    print('Run benchmarking for random_predict: ', end='')
    score_game(random_predict)
    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_core_v2)
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
