"""This file contain 2 function."""


def find_max(numbers):
    """Find MAX element in nubers list."""
    if len(numbers) == 0:
        return "Empty list"
    max_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i

    return max_num


def find_position(numbers, target):
    """Find target's position in numbers list."""
    position = -1
    count = 0

    for i in numbers:
        if i == target:
            position = count
            break
        else:
            count += 1

    return position


print(find_max([1, 2, 3, 4, 5, 8, 0, 4]))
print(find_max([1, 5, 3, 4, 20, 0, 0, 8]))
print(find_max([1, 5, 3, 400, 80, 80, 0, 4]))
print(find_max([]))
print(find_position([100, 20, 36, 48, 25, 80, 10, 14], 0))
print(find_position([100, 20, 36, 48, 25, 80, 10, 14], 20))
print(find_position([100, 20, 36, 48, 25, 80, 10, 14], 25))
