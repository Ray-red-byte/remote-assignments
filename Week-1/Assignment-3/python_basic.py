def find_max(numbers):
    max_num = numbers[0]
    for i in numbers:
        if (i > max_num):
            max_num = i

    return max_num

def find_position(numbers, target):
    position = -1
    count = 0
    for i in numbers:
        if (i == target):
            position = count
            break
        else:
            count = count + 1
    return position


print(find_max([1, 2, 3, 4, 5, 8, 0, 4])) 
print(find_position([1, 2, 3, 4, 5, 8, 0, 4], 0))