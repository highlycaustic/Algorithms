from random import randint


def bubble_sort(arr):
    """
    Сортировка пузырьком, имеет сложность порядка:

    В лучшем случае - O(n)

    В среднем случае - O(n^2)

    В худшем случае - O(n^2)

    :param arr: Массив для сортировки
    """
    for n in range(len(arr) - 1, 0, -1):
        swapped = False

        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break


def merge_sort(arr):
    """
    Сортировка слиянием, имеет сложность порядка:

    В лучшем случае - O(n log(n))

    В среднем случае - O(n log(n))

    В худшем случае - O(n log(n))
    :param arr: Массив для сортировки
    :return: Отсортированный массив
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Вспомогательная функция для merge_sort
    :param left: Левая половина массива
    :param right: Правая половина массива
    :return: Склеенный массив
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(array, low, high):
    """
    "Быстрый" алгоритм сортировки массива, имеет сложность порядка:

    В лучшем случае - O(n log(n))

    В среднем случае - O(n log(n))

    В худшем случае - O(n^2)
    :param array: Массив для сортировки
    :param low: Нижняя граница
    :param high: Верхняя граница
    :return:
    """
    if low < high:

        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)

        quick_sort(array, pi + 1, high)


def partition(array, low, high):
    """
    Вспомогательная функция для quick_sort
    :param array: Массив
    :param low: Нижняя граница
    :param high: Верхняя граница
    :return:
    """
    pivot = array[randint(low,high)]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def shell_sort(arr):
    """
    Сортировка Шелла, имеет сложность порядка:

    В лучшем случае - O(n log(n))

    В среднем случае - O(n(log(n))^2)

    В худшем случае - O(n(log(n))^2)
    :param arr: Массив для сортировки
    :return:
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2