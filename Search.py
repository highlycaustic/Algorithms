def seq_search(arr: list, x):
    for elem in arr:
        if elem == x:
            return arr.index(elem)
    return -1

def bin_search(arr, low, high, x):

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