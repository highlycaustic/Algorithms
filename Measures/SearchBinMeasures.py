import timeit

import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def measure_bin_search(size):
    import Arrays
    import Search
    from random import randint

    # Средний случай, поиск случайного числа в случайном массиве
    bin_search_avg_setup= """
low = 1
high = size
test_arr = Arrays.mono_raising_list(low, high, size)
x = randint(low, high * 100)
"""

    # Гарантированно найдет 1 в середине, массив состоит из единиц
    bin_search_best_setup= """
test_arr = [1] * size
x = 1
"""

    # Худший случай - поиск значения на краю массива
    bin_search_worst_setup= """
low = 1
high = 1
test_arr = Arrays.mono_raising_list(low, high, size)
test_arr[0] = 0
test_arr[-1] = size * 2
if (randint(0,1) == 0):
    x = 0
else:
    x = size * 2
"""

    # Выражение для замеров времени исполнения
    bin_search_stmt = """
Search.bin_search(test_arr, 0, len(test_arr) - 1, x)
"""

    repeat_count = 10
    result_avg = timeit.repeat(stmt=bin_search_stmt, setup=bin_search_avg_setup, repeat=repeat_count, number=1, globals=locals())
    result_best = timeit.repeat(stmt=bin_search_stmt, setup=bin_search_best_setup, repeat=repeat_count, number=1, globals=locals())
    result_worst = timeit.repeat(stmt=bin_search_stmt, setup=bin_search_worst_setup, repeat=repeat_count, number=1, globals=locals())

    result_avg_avg = sum(result_avg)/len(result_avg)
    result_best_avg = sum(result_best)/len(result_best)
    result_worst_avg = sum(result_worst)/len(result_worst)

    return result_avg_avg, result_best_avg, result_worst_avg

measure_steps = [10, 100, 500, 1000, 5000, 10_000, 25_000, 50_000, 75_000, 100_000, 150_000, 250_000, 500_000, 1_000_000]

pd_df = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])

for step in pd_df.index:
    result = measure_bin_search(step)
    pd_df.at[step, "avg"] = result[0]
    pd_df.at[step, "best"] = result[1]
    pd_df.at[step, "worst"] = result[2]

sns.set_theme()
sns.lineplot(markers=True, data=pd_df)
plt.show()