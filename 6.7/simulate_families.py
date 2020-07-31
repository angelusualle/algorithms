import random
# shows 50/50 split in gender population distribution
def simulate_families(n):
    num_men = 0
    num_women = 0
    for i in range(n):
        local_women = 0
        local_men = 0
        while local_women == 0:
            birth = random.choice(['m', 'w'])
            if birth == 'm':
                local_men += 1
            else:
                local_women += 1
        num_men += local_men
        num_women += local_women
    print(num_men)
    print(num_women)

if __name__ == '__main__':
    simulate_families(100000)