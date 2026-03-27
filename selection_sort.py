# UC8 – Compare Selection Sort performance with Bubble Sort.

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


def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def compare_performance():
    """
    Compare Selection Sort vs Bubble Sort.
    """
    size = 500
    arr = [random.randint(1, 1000) for _ in range(size)]

    arr1 = arr.copy()
    arr2 = arr.copy()

    # Selection Sort
    start = time.time()
    selection_sort(arr1)
    selection_time = time.time() - start

    # Bubble Sort
    start = time.time()
    bubble_sort(arr2)
    bubble_time = time.time() - start

    print(f"Input Size: {size}")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")


def main() -> None:
    compare_performance()


if __name__ == "__main__":
    main()