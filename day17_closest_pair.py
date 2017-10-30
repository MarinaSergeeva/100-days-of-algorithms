from math import sqrt, pow, isclose
import random

def get_closest_1d(array):
    """ special case - find the closest pair of points in 1-dimentional array
    """
    sorted_array = sorted(array)
    sorted_ind = get_indices_of_sorted_array(array)
    min_ind = 1
    min_dist = sorted_array[1] - sorted_array[0]
    for i in range(2, len(array)):
        cur_dist = sorted_array[i] - sorted_array[i - 1]
        if cur_dist < min_dist:
            min_dist = cur_dist
            min_ind = i
    return min_dist, (sorted_ind[min_ind - 1], sorted_ind[min_ind])

def get_indices_of_sorted_array(array):
    return [el[0] for el in sorted(enumerate(array), key=lambda x: x[1])]

def test_get_closest_1d():
    array = [0, 5, 2, 3, 8]
    assert get_closest_1d(array) == (1, (2, 3))

def get_closest_pair_2d(array):
    """ divide and conquer algorithm, running time O(nlogn)
    """
    array_x = sorted(array, key=lambda x: x[0]) # array sorted by x coordinate
    array_y = sorted(array, key=lambda x: x[1]) # sorted by y coordinate
    return get_closest_pair(array_x, array_y)

def compute_dist_2d(x, y):
    return sqrt(sum([pow(x[i] - y[i], 2) for i in range(2)]))

def get_closest_pair(array_x, array_y):
    if len(array_x) < 4:
        # end case, compute optimum by brute force
        min_dist = compute_dist_2d(array_x[0], array_x[1])
        min_pair = (array_x[0], array_x[1])
        for i in range(len(array_x)):
            for j in range(i + 1, len(array_x)):
                cur_dist = compute_dist_2d(array_x[i], array_x[j])
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_pair = (array_x[i], array_x[j])
        return min_dist, min_pair
    # split arrays in left and right halves
    med = len(array_x) // 2
    med_x = array_x[med][0]
    left_array_x = array_x[:med]
    right_array_x = array_x[med:]
    left_array_y = [el for el in array_y if el[0] <= med_x]
    right_arry_y = [el for el in array_y if el[0] > med_x]
    # get solutions for left and right subproblems and for splitted pairs
    left_solution = get_closest_pair(left_array_x, left_array_y)
    right_solution = get_closest_pair(right_array_x, right_arry_y)
    split_solution = get_split_pair(array_x, array_y, min(left_solution[0], right_solution[0]), med_x)
    if split_solution is None:
        return min([left_solution, right_solution], key=lambda x: x[0])
    return min([left_solution, right_solution, split_solution], key=lambda x: x[0])

def get_split_pair(array_x, array_y, delta, med_x):
    """returns a split pair if distance between points less then delta"""
    # consider only points in the central strip at most delta apart from the median x
    strip_y = [el for el in array_y if med_x - delta < el[0] < med_x + delta]
    min_dist = delta
    min_pair = None
    for i in range(len(strip_y) - 1):
        # compare only with points that are at most 7 positions apart
        for j in range(i + 1, min(i + 8, len(strip_y) - i)):
            cur_dist = compute_dist_2d(strip_y[i], strip_y[j])
            if cur_dist < min_dist:
                min_dist = cur_dist
                min_pair = (strip_y[i], strip_y[j])
    if min_pair is not None:
        return (min_dist, min_pair)

def test_compute_dist_2d():
    assert isclose(compute_dist_2d((0, 0), (4, 4)), sqrt(32))
    assert isclose(compute_dist_2d((0, 0), (0, 0)), 0)
    assert isclose(compute_dist_2d((1, 2), (2, 1)), sqrt(2))

def test_get_closest_pair_2d():
    array = [(0, 0), (1, 5), (3, 2), (5, 5), (8, 3), (9, 6), (10, 5)]
    result = get_closest_pair_2d(array)
    assert isclose(result[0], sqrt(2))
    assert result[1] == ((9, 6), (10, 5))

def test_get_closest_pair_2d_large_input():
    size = 10000
    array = [(random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)) for i in range(size)]
    res = get_closest_pair_2d(array)

if __name__ == "__main__":
    test_get_closest_1d()
    test_compute_dist_2d()
    test_get_closest_pair_2d()
    test_get_closest_pair_2d_large_input()
