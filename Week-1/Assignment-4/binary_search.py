"""This file contain Binary Search algorithm."""


def binary_search_position(numbers, target):
    """Use Binary Search to find target's position."""
    left_position = 0
    right_position = len(numbers) - 1

    while left_position <= right_position:
        middle_position = (left_position + right_position)//2
        if target == numbers[middle_position]:  # Hit the target
            return middle_position
        elif target > numbers[middle_position]:  # Search right part
            left_position = middle_position + 1
        elif target < numbers[middle_position]:  # Search left part
            right_position = middle_position - 1
    return -1  # Target not in numbers


print(binary_search_position([0, 5, 6, 10, 14, 48], 8))
print(binary_search_position([1, 4, 5, 50, 60, 100], 4))
print(binary_search_position([0, 9, 18, 19, 29, 48], 18))
print(binary_search_position([0, 5, 36, 50, 75, 80], 80))
