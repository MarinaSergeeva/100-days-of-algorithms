def count_inversions(array, low=0, high=None, sort=False):
    if high is None:
        # first call
        high = len(array)
        if not sort:
            # modify the pointers to sort a copy of the initial array
            array_copy = array[:]
            array = array_copy
    if low >= high - 1:
        return 0
    else:
        med = (high + low) // 2
        left_inversions = count_inversions(array, low, med)
        right_inversions = count_inversions(array, med, high)
        split_inversions = merge_sort_and_count(array, low, med, high)
        return left_inversions + right_inversions + split_inversions

def merge_sort_and_count(array, low, med, high):
    array1 = array[med - 1:(low - 1 if low - 1 >= 0 else None):-1]
    array2 = array[high - 1:med - 1:-1]
    i = low
    inversions_count = 0
    while array1 != [] and array2 != []:
        if array1[-1] <= array2[-1]:
            array[i] = array1.pop()
        else:
            array[i] = array2.pop()
            inversions_count += len(array1)
        i += 1
    array1 = array1 if array1 != [] else array2
    while array1 != []:
        array[i] = array1.pop()
        i += 1
    return inversions_count

def test_count_inversions():
    array = [1, 3, 5, 2, 4, 6]
    assert count_inversions(array) == 3
    sorted_array = list(range(3))
    assert count_inversions(sorted_array) == 0

if __name__ == "__main__":
    test_count_inversions()
