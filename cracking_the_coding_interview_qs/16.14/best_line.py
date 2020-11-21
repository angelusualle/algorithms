import math

def best_line(pts):
    lines = {}
    max_line = None
    max_line_cnt = 0
    for i, pt in enumerate(pts):
        for pt2 in pts[i+ 1:]:
            slope = abs((pt2[1] - pt[1])/(pt2[0] - pt[0]))
            intercept = pt2[1] - slope*pt2[0]
            val = str(slope) + ':' + str(intercept)
            if val in lines:
                lines[val] += 1
            else:
                lines[val] = 2
            if lines[val] > max_line_cnt:
                max_line_cnt = lines[val]
                max_line = val
    return max_line