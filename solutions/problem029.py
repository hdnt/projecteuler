import math


def solve(max_num=100):
    total = (max_num - 1)**2
    repeats = 0
    bases_found = set()
    for base in range(2, math.floor(math.sqrt(max_num)) + 1):
        if base not in bases_found:
            max_power = int(math.log(max_num)//math.log(base))
            prods_found = set([x for x in range(2, max_num+1)])
            for power in range(2, max_power + 1):
                bases_found.add(base**power)
                prods_found.update([power*x for x in range(2, max_num+1)])
            repeats += ((max_power * (max_num - 1)) - len(prods_found))
    return total - repeats
