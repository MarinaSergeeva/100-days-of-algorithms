"""edit distance and sequence alignmnet implementation"""

# possibe options for baktracking
DIAG, DOWN, LEFT = range(3)

def get_cost(symbol1, symbol2):
    """cost of replacing symbol1 and symbol2"""
    if symbol1 == symbol2:
        return 0
    return 2

def get_best_alignmnet(seq1, seq2):
    """returns the updated sequences for alignment and edit distance cost"""
    gap_penalty = 1
    penalties, backtraces = get_penalties_and_backtraces(seq1, seq2, gap_penalty)
    modified_sequences = backtrack(backtraces, seq1, seq2)
    return modified_sequences, penalties[-1][-1]

def get_penalties_and_backtraces(seq1, seq2, gap_penalty):
    """creates penalty matrix and backtrace marix using dymanic programming"""
    penalties = [[i * gap_penalty] + [0 for i in range(len(seq1))] for i in range(len(seq2) + 1)]
    penalties[0] = [i * gap_penalty for i in range(len(seq1) + 1)]
    backtraces = [[DOWN] + [0 for i in range(len(seq1))] for i in range(len(seq2) + 1)]
    backtraces[0] = [LEFT for i in range(len(seq1) + 1)]
    for i, el2 in enumerate(seq2):
        for j, el1 in enumerate(seq1):
            penalty_options = [penalties[i][j] + get_cost(el1, el2), #DIAG
                               penalties[i][j + 1] + gap_penalty, #DOWN
                               penalties[i + 1][j] + gap_penalty] #LEFT
            min_penalty = min(penalty_options)
            penalties[i + 1][j + 1] = min_penalty
            backtraces[i + 1][j + 1] = penalty_options.index(min_penalty)
    return penalties, backtraces

def backtrack(backtraces, seq1, seq2):
    """returns the updated sequences based on the best alignment"""
    j, i = len(seq1), len(seq2)
    modified_seq1 = []
    modified_seq2 = []
    while i > 0 and j > 0:
        if backtraces[i][j] == DIAG:
            modified_seq1.append(seq1[j - 1])
            modified_seq2.append(seq2[i - 1])
            i -= 1
            j -= 1
        elif backtraces[i][j] == DOWN:
            modified_seq2.append(" ")
            i -= 1
        else:
            modified_seq1.append(" ")
            j -= 1
    for _ in range(i):
        modified_seq2.append(" ")
    for _ in range(j):
        modified_seq1.append(" ")
    return "".join(modified_seq1[::-1]), "".join(modified_seq2[::-1])

def test_get_best_alignmnet():
    seq1_1 = "aaaaa"
    seq2_1 = "aaaaa"
    assert get_best_alignmnet(seq1_1, seq2_1) == (('aaaaa', 'aaaaa'), 0)
    seq1_2 = "aaaaa"
    seq2_2 = "aaa"
    assert get_best_alignmnet(seq1_2, seq2_2) == (('  aaa', 'aaa'), 2)
    seq1_3 = "aaab"
    seq2_3 = "aaba"
    assert get_best_alignmnet(seq1_3, seq2_3) == ((' aab', 'aab '), 2)

if __name__ == "__main__":
    test_get_best_alignmnet()
