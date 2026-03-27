# UC7 – Analyze time complexity of Selection Sort with different input sizes.

import time
import random


def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def analyze_performance():
    """
    Analyze execution time for different input sizes.
    """
    sizes = [100, 200, 500, 1000]

    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]

        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()

        print(f"Size: {size}, Time Taken: {end_time - start_time:.6f} seconds")


def main() -> None:
    analyze_performance()


if __name__ == "__main__":
    main()