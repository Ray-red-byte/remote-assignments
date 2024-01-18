"""This file contain Binary Search algorithm."""


def binary_search_first(numbers, target):
    """Use Binary Search to find target's position."""
    left_position = 0
    right_position = len(numbers) - 1

    while left_position <= right_position:
        middle_position = (left_position + right_position)//2
        if target == numbers[middle_position]:  # Hit the target
            count = middle_position
            while True:                         # Trace back to first
                count -= 1
                if target != numbers[count]:
                    return count + 1

        elif target > numbers[middle_position]:  # Search right part
            left_position = middle_position + 1

        elif target < numbers[middle_position]:  # Search left part
            right_position = middle_position - 1

    return left_position  # Target not in numbers


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 7))
print(binary_search_first([1, 2, 2, 5, 5, 6, 6, 6, 10], 6))
print(binary_search_first([1, 2, 2, 5, 5, 6, 6, 6, 10], 7))
