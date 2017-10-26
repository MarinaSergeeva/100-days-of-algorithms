from day07_quicksort import partition

def get_k_statistics(array, k, low=0, high=None):
    """ returns kth smallest element i the array (k can be from 1 to len(array))
    """
    if high is None:
        high = len(array)
    partition_index = partition(array, low, high)
    if partition_index == k - 1:
        return array[partition_index]
    elif partition_index > k - 1:
        return get_k_statistics(array, k, low, partition_index)
    else:
        return get_k_statistics(array, k, partition_index + 1, high)

def test_get_k_statistics():
    my_list = [3, 8, 1, 5, 2]
    assert get_k_statistics(my_list, 1, low=0, high=None) == 1
    assert get_k_statistics(my_list, 5, low=0, high=None) == 8
