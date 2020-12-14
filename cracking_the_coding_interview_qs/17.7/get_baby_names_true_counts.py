# O (N + E) where n is number of names and e is synonym connections.
def get_baby_names_true_counts(counts, synonyms):
    mapz = {}
    for name in counts:
        if name in synonyms:
            other_name = synonyms[name]
        else:
            mapz[name] = {'con': set(), 'val': counts[name]}
            continue
        if name not in mapz:
            mapz[name] = {'con': set([other_name]), 'val': counts[name]}
        elif other_name not in mapz[name]['con']:
            mapz[name]['con'].add(other_name)
        if other_name not in mapz:
            mapz[other_name] = {'con': set([name]), 'val': counts[other_name]}
        elif name not in mapz[other_name]['con']:
            mapz[other_name]['con'].add(name)
    ans = {}
    for k in mapz:
        if 'done' not in mapz[k]:
            next_to_process = [k]
            val = 0
        else:
            continue
        while next_to_process:
            item = next_to_process.pop()
            val += mapz[item]['val']
            mapz[item]['done'] = True
            for c in mapz[item]['con']:
                if 'done' not in mapz[c]:
                    next_to_process.append(c)
        ans[k] = val
    return ans