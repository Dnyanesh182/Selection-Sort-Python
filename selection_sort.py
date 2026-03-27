# UC5 – Apply Selection Sort on list of strings (lexicographical order).

def selection_sort_strings(arr: list[str]) -> list[str]:
    """
    Selection Sort for strings (lexicographical order).

    Time Complexity: O(n^2)
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main() -> None:
    arr = ["banana", "apple", "cherry", "date"]

    print(f"Original List: {arr}")
    sorted_arr = selection_sort_strings(arr)
    print(f"Sorted List: {sorted_arr}")


if __name__ == "__main__":
    main()