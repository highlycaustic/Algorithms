from random import randint


def random_list(low, high, size):
    """
    Создает массив случайных значений
    :param low: Нижний предел случайных значений
    :param high: Верхний предел случайных значений
    :param size: Размер массива
    :return: Массив со случайно сгенерированными числами
    """
    return [randint(low, high) for x in range(size)]


def mono_raising_list(low, high, size):
    """
    Создает массив из монотонно растущих случайных значений
    :param low: Нижний предел случайных значений
    :param high: Верхний предел случайных значений
    :param size: Размер массива
    :return: Массив с монотонно растущими случайно сгенерированными числами
    """
    return [(x + randint(low,high)) for x in range(size)]


def is_sorted(arr):
    """
    Проверяет, отсортирован ли массив по возрастанию значений
    :param arr: Массив для проверки
    :return: True - если массив отсортирован
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def save_to_file(arr, filename: str):
    """
    Построчно сохраняет массив в файл
    :param arr: Массив для сохранения
    :param filename: Имя файла
    :return:
    """
    with open(filename, 'w') as f:
        for elem in arr:
            f.write(f"{elem}\n")