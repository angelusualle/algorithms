# O(n) time and space through cache usage
def get_max_height(boxes, current_height=0, last_box= None, max_height=[0]):
    max_height[0] = max(max_height[0], current_height)
    for i in range(len(boxes)):
        if last_box is None or (last_box[0] < boxes[i][0] and last_box[1] < boxes[i][1] and last_box[2] < boxes[i][2]):
            boxes_copy = [x[:] for x in boxes]
            val = boxes_copy.pop(i)
            get_max_height(boxes_copy, current_height + val[2], val, max_height)
