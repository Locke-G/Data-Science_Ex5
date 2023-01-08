def find_single(arr):
    result = 0
    for element in arr:
        if isinstance(element, int):
            result ^= element
    return result

find_single([5, 2, 3, 2, 5, 3, 1])