# UC2 – Modify Selection Sort to sort array in descending order.

def selection_sort_desc(arr: list[int]) -> list[int]:
    """
    Perform Selection Sort in descending order.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        max_index = i

        # Find index of maximum element
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap if needed
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


def main() -> None:
    arr = [64, 25, 12, 22, 11]

    print(f"Original Array: {arr}")
    sorted_arr = selection_sort_desc(arr)
    print(f"Sorted Array (Descending): {sorted_arr}")


if __name__ == "__main__":
    main()