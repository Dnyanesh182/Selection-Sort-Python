# UC6 – Sort custom objects using Selection Sort with key (e.g., sort by age).

class Person:
    """
    Represents a person with name and age.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name}({self.age})"


def selection_sort_objects(arr: list, key) -> list:
    """
    Selection Sort for custom objects using key function.

    Time Complexity: O(n^2)
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_index]):
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main() -> None:
    people = [
        Person("John", 25),
        Person("Alice", 22),
        Person("Bob", 30),
        Person("Eve", 28)
    ]

    print(f"Original List: {people}")

    # Sort by age
    sorted_people = selection_sort_objects(people, key=lambda p: p.age)

    print(f"Sorted by Age: {sorted_people}")


if __name__ == "__main__":
    main()