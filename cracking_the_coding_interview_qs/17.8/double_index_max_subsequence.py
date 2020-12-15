# O(N^2) time and O(N^2) space
def double_index_max_subsequence(indices):
    indices.sort(key=lambda x: x[0])
    subsequences = {}
    for i, item in enumerate(indices):
        best = [item]
        max_len_term = 1
        for end in subsequences:
            if subsequences[end][-1][1] <= item[1]:
                base_seq = subsequences[end][:]
                if len(base_seq) + 1 > max_len_term:
                    base_seq.append(item)
                    best = base_seq
                    max_len_term = len(base_seq)
        subsequences[i] = best
    best = None
    best_len = float("-inf")
    for s in subsequences:
        if len(subsequences[s]) > best_len:
            best = subsequences[s]
            best_len = len(subsequences[s])
    return best