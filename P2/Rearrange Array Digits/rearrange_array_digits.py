def rearrange_digits(arr):
    if len(arr) < 2:
        return arr

    sorted_arr = merge_sort(arr)
    num1, num2 = get_two_numbers_from_array(sorted_arr)
    return [num1, num2]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] > right[0] else right.pop(0))
    return result + left + right


def get_two_numbers_from_array(arr):

    num1, num2 = 0, 0
    for i, digit in enumerate(arr):
        if i % 2 == 0:
            # multiplying by 10 to shift all the digits one place left
            num1 = num1 * 10 + digit
        else:
            num2 = num2 * 10 + digit
    return num1, num2


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
# pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# pass
test_function([[1, 2, 3], [31, 2]])
# pass
