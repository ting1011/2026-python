def linear_search(data: list, target) -> int:
    for i, v in enumerate(data):
        if v == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def set_search(data: list, target) -> bool:
    return target in data
