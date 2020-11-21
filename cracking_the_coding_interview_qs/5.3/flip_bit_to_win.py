def flip_bit_to_win(num):
    previous_count = 0
    current_count = 0
    max_len = 1
    while num != 0:
        digit = num & 1
        if digit:
            current_count += 1
        else:
            if num & 2 == 0:
                previous_count = 0
            else:
                previous_count = current_count
            current_count = 0
        max_len = max(current_count+previous_count+1, max_len)
        num >>= 1
    return max_len

