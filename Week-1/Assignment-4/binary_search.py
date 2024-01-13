def binary_search_position(numbers, target):
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
            