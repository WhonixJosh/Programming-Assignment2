import random

def simple_fill_descending(n):
    ints = []
    for i in range(1, n + 1):
        ints.append(i)
    return ints[::-1]

def random_fill(n):
    ints = []
    for i in range(0,n):
        int_to_add = random.randint(1, n + 1)
        while int_to_add in ints:
            int_to_add = random.randint(1, n + 1)
        ints.append(int_to_add)
    return ints