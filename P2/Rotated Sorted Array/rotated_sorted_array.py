
def rotated_array_search(input_list, target):
    left, right = 0, len(input_list) - 1

    while left <= right:
        # Floor Division
        mid = (left + right) // 2
        if input_list[mid] == target:
            return mid

        if is_left_half_sorted(input_list, left, mid):
            if target_in_left_half(input_list, target, left, mid):
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target_in_right_half(input_list, target, mid, right):
                left = mid + 1
            else:
                right = mid - 1

    return -1


def is_left_half_sorted(input_list, left, mid):
    return input_list[left] <= input_list[mid]


def target_in_left_half(input_list, target, left, mid):
    return input_list[left] <= target < input_list[mid]


def target_in_right_half(input_list, target, mid, right):
    return input_list[mid] < target <= input_list[right]


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# all pass
