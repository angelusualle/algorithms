# O(n) time O(1) space
def get_max_minutes(reqs):
    one_away = 0
    two_away = 0
    for req in reqs:
        best_with = req + two_away
        best_without = one_away
        curr = max(best_with, best_without)
        two_away = one_away
        one_away = curr
    return one_away

