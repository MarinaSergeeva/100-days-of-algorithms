def binary_search(array, el, low=0, high=None):
    """returns index of the element with the value el or None if the element is
    not in the list"""
    if high is None:
        high = len(array)
    if high - low <= 0:
        return None
    med = (low + high) // 2
    if array[med] == el:
        return med
    elif array[med] > el:
        return binary_search(array, el, low, med)
    else:
        return binary_search(array, el, med + 1, high)

def test_binary_search():
    my_list = [1, 2, 3, 5, 6, 8]
    assert binary_search(my_list, 5) == 3
    assert binary_search(my_list, 8) == 5
    assert binary_search(my_list, 1) == 0
    assert binary_search(my_list, 4) is None
