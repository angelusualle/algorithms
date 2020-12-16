from collections import deque
def get_kth_prime_factor_357_num(k):
    q3 = deque([3])
    q5 = deque([5])
    q7 = deque([7])
    i = 2
    ans = 1
    while i <= k:
        if q3[0] <= q5[0] and q3[0] <= q7[0]:
            num = q3[0]
            q3.append(num*q3[-1])
            q5.append(num*q5[-1])
            q7.append(num*q7[-1])
            q3.popleft()
        elif q5[0] <= q3[0] and q5[0] <= q7[0]:
            num = q5[0]
            q5.append(num*q5[-1])
            q7.append(num*q7[-1])
            q5.popleft()
        else:
            num = q7[0]
            q7.append(num*q7[-1])
            q7.popleft()
        i += 1
    return num