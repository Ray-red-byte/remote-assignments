
def count(input):
    hashmap = {}
    for i in input:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    return hashmap


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    hashmap = {}
    for item in input:
        if item["key"] not in hashmap:
            hashmap[item["key"]] = item["value"]
        else:
            hashmap[item["key"]] += item["value"]

    return hashmap


input2 = [
    {'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c',
                                                         'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}
]
print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
