from random import randint

def random_list(low, high, size):
    return [randint(low, high) for x in range(size)]

def mono_raising_list(low, high, size):
    return [(x + randint(low,high)) for x in range(size)]

def is_sorted(list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))

def save_to_file(list, filename: str):
    with open(filename, 'w') as f:
        for elem in list:
            f.write(f"{elem}\n")
