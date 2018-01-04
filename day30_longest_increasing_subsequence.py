"""Allgorithm that finds the longest increasing subsequence using dynamic programming"""

def longest_increasing_subseq(sequence):
    """returns the longest increasing subsequence and its length"""
    predecessors = []
    max_length = []
    for i, element in enumerate(sequence):
        pred = None
        cur_prev_len = 0
        for j in range(i):
            if sequence[j] < element:
                if cur_prev_len <= max_length[j]:
                    cur_prev_len = max_length[j]
                    pred = j
        predecessors.append(pred)
        max_length.append(cur_prev_len + 1)
    return get_max_subsequence(predecessors, max_length, sequence)

def get_max_subsequence(predecessors, max_length, sequence):
    """create the longest subsequence by tracking backpointers"""
    subsequence = []
    latest = max_length.index(max(max_length))
    subsequence.append(sequence[latest])
    prev_el = predecessors[latest]
    while prev_el is not None:
        cur_el = prev_el
        subsequence.append(cur_el)
        prev_el = predecessors[cur_el]
    return subsequence[::-1]

def test_longest_increasing_subseq():
    sequence = [2, 4, 3, 5, 1, 7, 6, 9, 8]
    assert longest_increasing_subseq(sequence) == [0, 2, 3, 6, 9]

if __name__ == "__main__":
    test_longest_increasing_subseq()
