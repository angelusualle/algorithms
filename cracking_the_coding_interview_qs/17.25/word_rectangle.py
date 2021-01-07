def word_rectangle(words):
    words_set = set(words)
    re_orderings = []
    heap_permutation(words, len(words), re_orderings)
    ans = (0, None, None)
    for wordz in re_orderings:
        for i in range(len(wordz)):
            for j in range(i+1, len(wordz)):
                longest_size = 0
                for w in wordz[i:j]:
                    if len(w) > longest_size:
                        longest_size = len(w)
                for y in range(longest_size):
                    for z in range(y+1, longest_size):
                        valid  = True
                        if len(wordz[i:j]) <= 0:
                            continue
                        len_ = len(wordz[i:j][0][y:z])
                        size = 0
                        wz = []
                        for w in wordz[i:j]:
                            if len(w[y:z]) != len_:
                                valid = False
                                break
                            if w[y:z] not in words_set:
                                valid = False
                                break
                            size += len(w[y:z])
                            wz.append(w[y:z])
                        if valid:
                            for i in range(len_):
                                wordiz = []
                                for wi in wz:
                                    wordiz.append(wi[i])
                                if ''.join(wordiz) not in words_set:
                                    valid = False
                                    break
                        
                        if valid and size > ans[0]:
                            ans = (size, wordz[i:j], (y,z))
    return ans

def heap_permutation(arr, size, ans):
    if size == 1:
        ans.append(arr)
        return
    for i in range(size):
        heap_permutation(arr[:], size-1, ans)
        if size % 2 == 1:
            arr[0], arr[size-1] = arr[size-1], arr[0]
        else:
            arr[i], arr[size-1] = arr[size-1], arr[i]