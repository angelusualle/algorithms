import random as r

def rand7():
    sums = 0
    for i in range(35):
        sums += rand5()
    return sums % 7
    

def rand5():
    return r.randint(0,4)