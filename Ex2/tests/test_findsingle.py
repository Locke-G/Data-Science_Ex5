from findsingle import find_single

def test_find_single():
    # Test for array with single element
    assert find_single([5]) == 5

    # Test for non non integer in array 
    assert find_single(['abc']) == 'abc'
    assert find_single([1, 'abc', 3, 1, 2, 4, 4]) == 3

    # Test for array with multiple elements
    assert find_single([5, 2, 3, 2, 5, 3, 1]) == 1
    assert find_single([1, 2, 3, 1, 2, 4, 4]) == 3
    assert find_single([1, 2, 3, 1, 2]) == 3
    
    # Test for empty array
    assert find_single([]) == 0

    # Test for array with all integers occurring exactly twice
    assert find_single([5, 2, 3, 2, 5, 3]) == 0
