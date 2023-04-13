import random


def get_min_max(ints):
    if type(ints) != list:
        return -1
    if len(ints) == 0:
        return -1

    min_val = max_val = ints[0]

    for num in ints[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)


l = [i for i in range(0, 10)]

random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print("Pass" if (-1 == get_min_max([])) else "Fail")
print("Pass" if (-1 == get_min_max(43)) else "Fail")
