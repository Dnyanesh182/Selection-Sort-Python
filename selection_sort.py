# UC10 – Refactor Selection Sort implementation using clean code practices and reusable functions.

from typing import Callable, Any, List


def should_swap(a: Any, b: Any, key: Callable, reverse: bool) -> bool:
    """
    Determine whether two elements should be swapped based on key and order.
    """
    return key(a) > key(b) if not reverse else key(a) < key(b)


def selection_sort(
    arr: List[Any],
    key: Callable = lambda x: x,
    reverse: bool = False
) -> List[Any]:
    """
    Generic Selection Sort implementation.

    Args:
        arr: List of elements
        key: Function to extract comparison value
        reverse: Sort in descending order if True

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        selected_index = i

        for j in range(i + 1, n):
            if should_swap(arr[selected_index], arr[j], key, reverse):
                selected_index = j

        if selected_index != i:
            arr[i], arr[selected_index] = arr[selected_index], arr[i]

    return arr


def main() -> None:
    # Integer sorting
    arr = [64, 25, 12, 22, 11]
    print("Ascending:", selection_sort(arr.copy()))
    print("Descending:", selection_sort(arr.copy(), reverse=True))

    # Custom object sorting
    people = [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 30},
    ]

    sorted_people = selection_sort(people, key=lambda x: x["age"])
    print("Sorted by age:", sorted_people)


if __name__ == "__main__":
    main()