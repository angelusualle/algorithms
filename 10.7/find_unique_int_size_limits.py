def find_unique_int_size_limits(input_batches):
    i = 0
    while i*62500000 < 4294967294:
        set_to_check = set(list(range(i*62500000, i*62500000+62500000)))
        for batch in input_batches:
            for element in batch:
                if element in set_to_check:
                    set_to_check.remove(element)
        if len(set_to_check):
            return set_to_check.pop()
        i += 1
    

