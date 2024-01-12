def binary_search_position(numbers, target):
    if (len(numbers)%2 == 0):
        middle_position = len(numbers)/2
        left = numbers[:middle_position]
        right = numbers[middle_position:]
    else:
        middle_position = len(numbers)/2 + 1
        left = numbers[:middle_position]
        right = numbers[middle_position:]

        if (numbers[middle_position] == target)
    
    