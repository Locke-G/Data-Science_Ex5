import pytest

def find_single(arr):
    result = 0
    for element in arr:
        if isinstance(element, int):
            result ^= element
    return result


def test_find_single():
    # Test for array with single element
    assert find_single([5]) == 5

    # Test for noninteger in array 
    assert find_single(['abc']) == 0
    assert find_single([1, 'abc', 3, 1, 2, 2, 4, 4]) == 3

    # Test for array with multiple elements
    assert find_single([5, 2, 3, 2, 5, 3, 1]) == 1
    assert find_single([1, 2, 3, 1, 2, 4, 4]) == 3
    assert find_single([1, 2, 3, 1, 2]) == 3
    
    # Test for empty array
    assert find_single([]) == 0

    # Test for array with all integers occurring exactly twice
    assert find_single([5, 2, 3, 2, 5, 3]) == 0
