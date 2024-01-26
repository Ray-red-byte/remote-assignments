def twoSum(nums, target):
    hashmap = {}  # num: id

    for id, i in enumerate(nums):
        remain = target - i
        if remain in hashmap:
            return [hashmap[remain], id]

        hashmap[i] = id
    return "Find No Answer"


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 7, 11, 15], 30))
print(twoSum([4, 7, 5, 80], 87))
