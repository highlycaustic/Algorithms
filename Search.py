def seq_search(arr: list, x):
    """
    Последовательный поиск, имеет сложность порядка:\n
    В лучшем случае - O(1)\n
    В среднем случае - O(n)\n
    В худшем случае - O(n)\n
    :param arr: Массив, по которому осуществляется поиск
    :param x: Искомое значение
    :return: Индекс найденного значения
    """
    for elem in arr:
        if elem == x:
            return arr.index(elem)
    return -1


def bin_search(arr, low, high, x):
    """
    Бинарный поиск, имеет сложность порядка:
    В лучшем случае - O(1)\n
    В среднем случае - O(log(n))\n
    В худшем случае - O(log(n))\n
    :param arr: Массив, по которому осуществляется поиск
    :param low: Нижняя граница поиска (начало массива)
    :param high: Верхняя граница поиска (конец массива)
    :param x: Искомое значение
    :return: Индекс найденного значения
    """
    if high >= low:

        # Средняя позиция
        mid = (high - low) // 2 + low

        # Если элемент найден в средней позиции
        if arr[mid] == x:
            return mid

        # Поиск слева
        elif arr[mid] > x:
            return bin_search(arr, low, mid - 1, x)

        # Поиск справа
        else:
            return bin_search(arr, mid + 1, high, x)

    else:
        # Вернуть -1 если элемент не найден
        return -1