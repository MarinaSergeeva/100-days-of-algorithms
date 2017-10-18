def partition(array, low, high):
    # uses array[low] element for the partition
    pivot = array[low]
    repl_index = low
    for i in range(low + 1, high):
        if array[i] < pivot:
            repl_index += 1
            array[i], array[repl_index] = array[repl_index], array[i]
    array[low], array[repl_index] = array[repl_index], array[low]
    return repl_index

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array)
    if low < high - 1:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index)
        quick_sort(array, partition_index + 1, high)

def test_quicksort():
    my_list = [3, 8, 1, 5, 2]
    quick_sort(my_list)
    assert my_list == [1, 2, 3, 5, 8]
