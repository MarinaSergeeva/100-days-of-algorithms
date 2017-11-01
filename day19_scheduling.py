def schedule(tasks):
    """schedues tasks to minimize sum(weight_i * completion_time_i)
    expected input - list of tuples (weight, time_to_complete)
    """
    ordering = [(i, el[1] / el[0]) for (i, el) in enumerate(tasks)]
    ordering = [el[0] for el in sorted(ordering, key=lambda x: x[1])]
    time_elapsed = 0
    weighted_sum_of_completion_times = 0
    for i in ordering:
        time_elapsed += tasks[i][1]
        weighted_sum_of_completion_times += tasks[i][0] * time_elapsed
    return ordering, weighted_sum_of_completion_times

def test_schedule():
    tasks0 = [(1, 3), (1, 2), (1, 7)]
    assert schedule(tasks0) == ([1, 0, 2], 19)
    tasks1 = [(3, 1), (2, 1), (7, 1)]
    assert schedule(tasks1) == ([2, 0, 1], 19)
    tasks2 = [(3, 5), (1, 2)]
    assert schedule(tasks2) == ([0, 1], 22)

if __name__ == "__main__":
    test_schedule()
