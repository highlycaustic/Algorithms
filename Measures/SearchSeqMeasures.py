import timeit

import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def measure_seq_search(size):
    import Arrays
    import Search
    from random import randint

    # Средний случай, поиск случайного числа в случайном массиве
    seq_search_avg_setup= """
low = 0
high = size * 100
test_arr = Arrays.random_list(low, high, size)
x = randint(low, high)
"""

    # Гарантированно найдет 1 в начале массива, массив состоит из единиц
    seq_search_best_setup= """
low = 1
high = 1
test_arr = Arrays.random_list(low, high, size)
x = randint(low, high)
"""

    # Гарантированно ничего не найдет, ищет 2 среди массива единиц
    seq_search_worst_setup= """
low = 1
high = 1
test_arr = Arrays.random_list(low, high, size)
x = randint(2, 2)
"""

    # Выражение для замеров времени исполнения
    seq_search_stmt = """
Search.seq_search(test_arr, x)
"""

    repeat_count = 15
    result_avg = timeit.repeat(stmt=seq_search_stmt, setup=seq_search_avg_setup, repeat=repeat_count, number=1, globals=locals())
    result_best = timeit.repeat(stmt=seq_search_stmt, setup=seq_search_best_setup, repeat=repeat_count, number=1, globals=locals())
    result_worst = timeit.repeat(stmt=seq_search_stmt, setup=seq_search_worst_setup, repeat=repeat_count, number=1, globals=locals())

    result_avg_avg = sum(result_avg)/len(result_avg)
    result_best_avg = sum(result_best)/len(result_best)
    result_worst_avg = sum(result_worst)/len(result_worst)

    return result_avg_avg, result_best_avg, result_worst_avg

measure_steps = [10, 100, 501, 1000, 5001, 10_000, 25_001, 50_000, 75_001, 100_000, 150_000, 250_000, 500_000, 1_000_000]

pd_df = pandas.DataFrame(index=measure_steps, columns=["avg", "best", "worst"])

for step in pd_df.index:
    result = measure_seq_search(step)
    pd_df.at[step, "avg"] = result[0]
    pd_df.at[step, "best"] = result[1]
    pd_df.at[step, "worst"] = result[2]

sns.set_theme()
sns.lineplot(markers=True, data=pd_df)
plt.show()