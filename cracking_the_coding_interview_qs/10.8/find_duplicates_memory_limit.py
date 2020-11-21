from bitarray import bitarray
def find_duplicates_memory_limit(arr, dups = []):
    bit_array = bitarray(32000)
    bit_array.setall(0)
    for item in arr:
        if bit_array[item]:
            dups.append(item)
        else:
            bit_array[item] = 1
    return dups