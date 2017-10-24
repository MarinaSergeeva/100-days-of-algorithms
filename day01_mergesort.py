def merge_sort(array, low=0, high=None):
    if high is None:
        high = len(array)
    if high - low > 1:
        med = (high + low) // 2
        merge_sort(array, low, med)
        merge_sort(array, med, high)
        merge(array, low, med, high)

def merge(array, low, med, high):
    array1 = array[med - 1:(low - 1 if low - 1 >=0 else None):-1]
    array2 = array[high - 1:med - 1:-1]
    i = low
    while array1 != [] and array2 != []:
        if array1[-1] < array2[-1]:
            array[i] = array1.pop()
        else:
            array[i] = array2.pop()
        i += 1
    if array1 != []:
        for j in range(i, high):
            array[j] = array1.pop()
    if array2 != []:
        for j in range(i, high):
            array[j] = array2.pop()

def test_merge_sort():
    my_list = [3, 8, 1, 5, 2]
    merge_sort(my_list)
    assert my_list == [1, 2, 3, 5, 8]
    
