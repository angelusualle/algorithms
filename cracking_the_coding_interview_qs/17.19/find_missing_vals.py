# O(N) time O(1) space
def find_missing_vals(n, arr):
    total = sum(arr)
    calc_total = n*(n+1)/2
    x_p_y = calc_total - total
    if x_p_y not in arr:
        return x_p_y
    product = prod(arr)
    calc_prod = prod(list(range(1,n+1)))
    xy = calc_prod / product
    # solving now
    # x + y = x_p_y
    # x*y = xy
    # y = x_p_y - x
    # x*(x_p_y - x) = xy
    # -x^2 + x*x_p_y - xy = 0
    # quadratic equation solver: 
    # a*x^2 + b*x + c
    # x,y = (-b +- sqrt(b^2 - 4*a*c)) / 2a\
    # solves for both x and y + or - lets do + for x and pull it out for y
    x = (-x_p_y + (x_p_y**2 - 4 * -1 * -xy)**.5) / 2 / -1
    y = (-x_p_y - (x_p_y**2 - 4 * -1 * -xy)**.5) / 2 / -1
    return x,y

def prod(arr):
    ans = 1
    for n in arr:
        ans*= n
    return ans

''' Below performs iteration rather than raw calculations
def find_missing_vals(n, arr):
    total = sum(arr)
    calc_total = n*(n+1)/2
    diff = calc_total - total
    if diff not in arr:
        return diff
    project = 1
    for num in arr:
        if num != project:
            return project, calc_total - total
        project += 1
'''