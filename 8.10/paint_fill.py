def paint_fill(arr, point, new_color, old_color = None):
    if point[0] > len(arr) - 1 or point[0] < 0 or point[1] > len(arr[0]) - 1 or point[1] < 0:
        return
    if old_color is None:
        old_color = arr[point[0]][point[1]]
    if arr[point[0]][point[1]] == old_color:
        arr[point[0]][point[1]] = new_color
        paint_fill(arr, (point[0] + 1, point[1]), new_color, old_color)
        paint_fill(arr, (point[0] - 1, point[1]), new_color, old_color)
        paint_fill(arr, (point[0], point[1] + 1), new_color, old_color)
        paint_fill(arr, (point[0], point[1] - 1), new_color, old_color)
