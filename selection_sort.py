# UC9 – Optimize Selection Sort logic (avoid unnecessary swaps).

def optimized_selection_sort(arr: list[int]) -> list[int]:
    """
    Optimized Selection Sort.

    Avoids unnecessary swaps.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    swaps = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Only swap when needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    print(f"Total Swaps: {swaps}")
    return arr


def main() -> None:
    arr = [64, 25, 12, 22, 11]

    print(f"Original Array: {arr}")
    sorted_arr = optimized_selection_sort(arr)
    print(f"Sorted Array: {sorted_arr}")


if __name__ == "__main__":
    main()