# O(n^2) time and O(1) space
def sort_stack(stack):
    if stack is None or len(stack) == 0:
        return stack
    temp_stack = []
    max_item = stack.pop()
    len_stack = 1
    while len(stack) > 0:
        item = stack.pop()
        if item > max_item:
            temp_stack.append(max_item)
            max_item = item
        else:
            temp_stack.append(item)
        len_stack += 1
    stack.append(max_item)
    while len(temp_stack) > 0:
        stack.append(temp_stack.pop())
    num_passes = 1
    while num_passes < len_stack:
        num_items = len_stack - num_passes
        max_item = stack.pop()
        while len(stack) > num_items:
            item = stack.pop()
            if item > max_item:
                temp_stack.append(max_item)
                max_item = item
            else:
                temp_stack.append(item)
        stack.append(max_item)
        while len(temp_stack) > 0:
            stack.append(temp_stack.pop())
        num_passes += 1
    return stack