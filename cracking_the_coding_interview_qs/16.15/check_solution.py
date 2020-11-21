from collections import defaultdict

def check_solution(sol, guess):
    hits = 0
    psuedo_hits = 0
    matcher = defaultdict(int)
    for i,let in enumerate(sol):
        if let == guess[i]:
            hits += 1
            continue
        elif matcher[guess[i]] > 0:
            psuedo_hits += 1
            matcher[guess[i]] -= 1
        matcher[let] += 1
    return hits, psuedo_hits