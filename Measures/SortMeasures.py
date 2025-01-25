import sys
import timeit

import pandas
import seaborn as sns
import matplotlib.pyplot as plt

sys.setrecursionlimit(110000)


def measure_sort(size, mode: str = 'quick'):
    import Arrays
    import Sort
    from random import randint

    # Средний случай - массив случайных чисел
    sort_avg_setup= """
low = 1
high = size
test_arr = Arrays.random_list(low, high, size)
"""

    # Лучший случай - массив уже отсортирован
    sort_best_setup= """
test_arr = [i for i in range(size)]
"""

    # Худший случай - массив отсортирован в обратном порядке
    sort_worst_setup= """
test_arr = [i for i in range(size, 0, -1)]
"""

    # Выражение для замеров времени исполнения

    repeat_count = 10

    if mode == 'bubble':
        sort_stmt = """
Sort.bubble_sort(test_arr)
"""
    elif mode == 'merge':
        sort_stmt = """
test_arr = Sort.merge_sort(test_arr)
"""
    elif mode == 'quick':
        sort_stmt = """
Sort.quick_sort(test_arr, 0, len(test_arr) - 1)
"""
    elif mode == 'shell':
        sort_stmt = """
Sort.shell_sort(test_arr)
"""
    sort_result_avg = timeit.repeat(stmt=sort_stmt, setup=sort_avg_setup, repeat=repeat_count, number=1, globals=locals())
    sort_result_best = timeit.repeat(stmt=sort_stmt, setup=sort_best_setup, repeat=repeat_count, number=1, globals=locals())
    sort_result_worst = timeit.repeat(stmt=sort_stmt, setup=sort_worst_setup, repeat=repeat_count, number=1, globals=locals())

    sort_result_avg_avg = sum(sort_result_avg)/len(sort_result_avg)
    sort_result_best_avg = sum(sort_result_best)/len(sort_result_best)
    sort_result_worst_avg = sum(sort_result_worst)/len(sort_result_worst)

    return sort_result_avg_avg, sort_result_best_avg, sort_result_worst_avg

measure_steps = [10, 100, 500, 1000, 2000, 5000, 10_000, 25_000, 50_000, 100_000]

data_bubble = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])
data_merge = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])
data_quick = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])
data_shell = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])

for step in data_bubble.index:
    result = measure_sort(step, 'bubble')
    data_bubble.at[step, "avg"] = result[0]
    data_bubble.at[step, "best"] = result[1]
    data_bubble.at[step, "worst"] = result[2]

for step in data_merge.index:
    result = measure_sort(step, 'merge')
    data_merge.at[step, "avg"] = result[0]
    data_merge.at[step, "best"] = result[1]
    data_merge.at[step, "worst"] = result[2]

for step in data_quick.index:
    result = measure_sort(step, 'quick')
    data_quick.at[step, "avg"] = result[0]
    data_quick.at[step, "best"] = result[1]
    data_quick.at[step, "worst"] = result[2]

for step in data_shell.index:
    result = measure_sort(step, 'shell')
    data_shell.at[step, "avg"] = result[0]
    data_shell.at[step, "best"] = result[1]
    data_shell.at[step, "worst"] = result[2]

sns.set_theme()

fig, axes = plt.subplots(2, 2, figsize=(18, 5))

sns.lineplot(markers=True, data=data_bubble, ax=axes[0,0])
axes[0,0].set_title("Bubble")

sns.lineplot(markers=True, data=data_merge, ax=axes[0,1])
axes[0,1].set_title("Merge")

sns.lineplot(markers=True, data=data_quick, ax=axes[1,0])
axes[1,0].set_title("Quick")

sns.lineplot(markers=True, data=data_shell, ax=axes[1,1])
axes[1,1].set_title("Shell")

plt.show()