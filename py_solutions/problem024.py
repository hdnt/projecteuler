from math import factorial as fac


def solve(target_pos):
    digits = [_ for _ in "0123456789"]
    res = []
    block = 0
    for rem_digits in range(len(digits), 1, -1):
        cur_block_size = fac(rem_digits)
        start_of_block = (block * cur_block_size)
        target_pos -= start_of_block
        sub_block_size = fac(rem_digits - 1)
        block = target_pos // sub_block_size
        res.append(digits[block])
        digits.remove(digits[block])
    return "".join(res) + digits[0]


if __name__ == "__main__":
    print(solve(10**6 - 1))
