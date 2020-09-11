from collections import defaultdict

# O(nlogn) where n is number of people for runtime, constant space, if r is unbounded may be better
def find_max_living_year(years):
    births = [x[0] for x in years]
    deaths = [x[1] for x in years if x[1] is not None]
    births.sort()
    deaths.sort()
    i = 0
    j = 0
    current_lives = 0
    max_year = -1
    max_curr = -1
    while i < len(births):
        if births[i] <= deaths[j]:
            current_lives += 1
            if current_lives > max_curr:
                max_year = births[i]
                max_curr = current_lives
            i += 1
        elif births[i] > deaths[j]:
            current_lives -= 1
            j += 1
    return max_year

'''
# O(rn) time and O(r) space where n is number of people and r is range
# if r is bounded this is best
def find_max_living_year(years):
    year_num = defaultdict(int)
    max_year = None
    max_val = 0
    for i in range(1900, 2001):
        year_num[i] = len([x[0] for x in years if x[0] <= i and (x[1] is  None or i <= x[1])])
        if year_num[i] > max_val:
            max_year = i
            max_val = year_num[i]
    return max_year
'''