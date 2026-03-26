# UC1 – Implement basic Selection Sort to sort an array in ascending order.

def selection_sort(arr: list[int]) -> list[int]:
    """
    Perform Selection Sort in ascending order.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find index of minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main() -> None:
    arr = [64, 25, 12, 22, 11]

    print(f"Original Array: {arr}")
    sorted_arr = selection_sort(arr)
    print(f"Sorted Array: {sorted_arr}")


if __name__ == "__main__":
    main()