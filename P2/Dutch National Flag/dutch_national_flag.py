def sort_flags(input_list):
    left, mid, right = 0, 0, len(input_list) - 1

    while mid <= right:
        if is_flag_0(input_list[mid]):
            input_list[left], input_list[mid] = input_list[mid], input_list[left]
            left += 1
            mid += 1
        elif is_flag_1(input_list[mid]):
            mid += 1
        else:
            input_list[mid], input_list[right] = input_list[right], input_list[mid]
            right -= 1

    return input_list


def is_flag_0(flag):
    return flag == 0


def is_flag_1(flag):
    return flag == 1


def test_function(test_case):
    sorted_array = sort_flags(test_case)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# pass
