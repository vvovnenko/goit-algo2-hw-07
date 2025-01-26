import random
import time

from lru import LRUCache


def range_sum_no_cache(array: list, L: int, R: int):
    sub_array = array[L:R]
    return sum(sub_array)


def update_no_cache(array: list, index: int, value: int):
    array[index] = value
    return array


cache = LRUCache(1000)


def range_sum_with_cache(array: list, L: int, R: int):
    key = (L, R)
    cached_sum = cache.get(key)

    if cached_sum != -1:
        return cached_sum

    range_sum = range_sum_no_cache(array, L, R)

    cache.put(key, range_sum)

    return range_sum


def update_with_cache(array: list, index: int, value: int):
    cache.cache_clear()
    array[index] = value
    return array


if __name__ == "__main__":

    N = 100000
    Q = 50000

    array = [random.randint(1, 100) for _ in range(N)]

    operations = []

    for _ in range(Q):
        if random.choice(["Range", "Update"]) == "Range":
            left = random.randint(0, N - 1)
            right = random.randint(left, N - 1)
            operations.append(("Range", left, right))
        else:
            index = random.randint(0, N - 1)
            value = random.randint(1, 100)
            operations.append(("Update", index, value))

    start_time = time.time()

    for operation in operations:
        if operation[0] == "Range":
            _, left, right = operation
            range_sum_no_cache(array, left, right)
        elif operation[0] == "Update":
            _, index, value = operation
            update_no_cache(array, index, value)
    end_time = time.time()
    time_no_cache = end_time - start_time

    start_time = time.time()
    for operation in operations:
        if operation[0] == "Range":
            _, left, right = operation
            range_sum_with_cache(array, left, right)
        elif operation[0] == "Update":
            _, index, value = operation
            update_with_cache(array, index, value)
    end_time = time.time()
    time_with_cache = end_time - start_time

    print("=" * 44)
    print(f"| Час виконання без кешування: {time_no_cache:.2f} секунд |")
    print(f"| Час виконання з LRU-кешем: {time_with_cache:.2f} секунд   |")
    print("=" * 44)
