import time
import matplotlib.pyplot as plt
from functools import lru_cache
from splay_tree import SplayTree


@lru_cache()
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree: SplayTree):
    cached_result = tree.find(n)
    if cached_result is not None:
        return cached_result

    if n <= 1:
        value = n
    else:
        value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)

    tree.insert(n, value)
    return value


def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time


def display_results(array, result_lru, result_st):
    print("n         LRU Cache Time (s)          Splay Tree Time (s)")
    print("{:-^50}".format(""))
    for i, n in enumerate(array):
        print(f"{n:>3}{result_lru[i]:^30.6f}{result_st[i]:^30.6f}")


def plot_results(array, result_lru, result_st):
    plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")
    plt.plot(array, result_lru, color="blue", label="LRU Cache")
    plt.plot(array, result_st, color="orange", label="Splay Tree")
    plt.xlabel("Число Фібоначчі (n)")
    plt.ylabel("Середній час виконання (секунди)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    tree = SplayTree()
    step = 50
    max_iterations = 19

    # Генерація масиву значень
    array = [i * step for i in range(max_iterations)]

    # Обчислення часу виконання для кожного алгоритму
    result_lru = []
    result_st = []

    for n in array:
        _, time_lru = measure_execution_time(fibonacci_lru, n)
        _, time_st = measure_execution_time(fibonacci_splay, n, tree)
        result_lru.append(time_lru)
        result_st.append(time_st)

    # Виведення результатів
    display_results(array, result_lru, result_st)

    # Побудова графіків
    plot_results(array, result_lru, result_st)
