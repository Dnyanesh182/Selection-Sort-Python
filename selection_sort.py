# UC3 – Count number of comparisons and swaps performed during sorting.

def selection_sort_with_metrics(arr: list[int]) -> tuple[list[int], int, int]:
    """
    Selection Sort with performance metrics.

    Returns:
    - sorted array
    - number of comparisons
    - number of swaps

    Time Complexity: O(n^2)
    """
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps


def main() -> None:
    arr = [64, 25, 12, 22, 11]

    print(f"Original Array: {arr}")
    sorted_arr, comparisons, swaps = selection_sort_with_metrics(arr)

    print(f"Sorted Array: {sorted_arr}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")


if __name__ == "__main__":
    main()