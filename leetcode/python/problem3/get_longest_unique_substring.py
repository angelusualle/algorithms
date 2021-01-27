# O(n) time and space where n is number of chars
def get_longest_unique_substring(s):
    start_index = 0
    end_index = 0
    answer = 0
    char_to_position = {}
    for i,let in enumerate(s):
        if let not in char_to_position:
            char_to_position[let] = i
        elif char_to_position[let] >= start_index:
            start_index = char_to_position[let] + 1
            char_to_position[let] = i
        else:
            char_to_position[let] = i
        end_index += 1
        if end_index - start_index > answer:
            answer = end_index - start_index
    return answer
            