# UC4 – Handle sorting of duplicate elements correctly.

def selection_sort(arr: list[int]) -> list[int]:
    """
    Selection Sort handling duplicate elements correctly.

    Time Complexity: O(n^2)
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            # Strict comparison ensures correct duplicate handling
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main() -> None:
    arr = [64, 25, 12, 22, 11, 25, 12]

    print(f"Original Array: {arr}")
    sorted_arr = selection_sort(arr)
    print(f"Sorted Array: {sorted_arr}")


if __name__ == "__main__":
    main()