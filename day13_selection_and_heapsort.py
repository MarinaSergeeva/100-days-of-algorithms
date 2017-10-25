import heapq

def selection_sort(array):
    for i in range(len(array)):
        min_index = find_min_index(array, i, len(array))
        array[i], array[min_index] = array[min_index], array[i]

def find_min_index(array, start, end):
    min_index = start
    min_element = array[start]
    for i in range(start + 1, end):
        if array[i] < min_element:
            min_index = i
            min_element = array[i]
    return min_index

def heapsort(array):
    heap = array[:]
    heapq.heapify(heap)
    sorted_array = []
    for i in range(len(array)):
        array[i] = heapq.heappop(heap)

def test_selection_sort():
    my_list = [3, 8, 1, 5, 2]
    selection_sort(my_list)
    assert my_list == [1, 2, 3, 5, 8]

def test_heapsort():
    my_list = [3, 8, 1, 5, 2]
    heapsort(my_list)
    assert my_list == [1, 2, 3, 5, 8]
