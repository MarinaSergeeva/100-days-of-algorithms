def get_knapsack(items, capacity):
    # items = [(value_i, weight_i),]
    optimal_values = [[0 for i in range(capacity + 1)]]
    optimal_solutions = []
    for i in range(1, len(items) + 1):
        cur_value = []
        cur_solution = []
        for j in range(capacity + 1):
            if items[i - 1][1] > j:
                cur_value.append(optimal_values[i - 1][j])
                cur_solution.append(False)
            else:
                if optimal_values[i - 1][j] > items[i - 1][0] + optimal_values[i - 1][j - items[i - 1][1]]:
                    cur_value.append(optimal_values[i - 1][j])
                    cur_solution.append(False)
                else:
                    cur_value.append(items[i - 1][0] + optimal_values[i - 1][j - items[i - 1][1]])
                    cur_solution.append(True)
        optimal_values.append(cur_value)
        optimal_solutions.append(cur_solution)
    solution_set = get_set(items, capacity, optimal_values, optimal_solutions)
    return solution_set, optimal_values[-1][-1]

def get_set(items, capacity, optimal_values, optimal_solutions):
    j = capacity
    solution_set = []
    for i in range(1, len(items) + 1):
        if optimal_solutions[-i][j]:
            solution_set.append(len(items) - i)
            j -= items[len(items) - i][1]
    return solution_set[::-1]

def test_get_knapsack():
    items = [(20, 20), (4, 3), (2, 5), (3, 3)]
    capacity = 6
    assert get_knapsack(items, capacity) == ([1, 3], 7)

if __name__ == "__main__":
    test_get_knapsack()
