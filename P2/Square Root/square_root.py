
def square_root(input):
    if type(input) != int:
        return "Please provide a number"
    if input < 0:
        return ("Please provide a number greater than zero")

    # we devide by two since it is the best possible guess
    guess = input / 2.0

    while desired_accuracy_reached(input, guess) == False:

        guess = newton_raphson(input, guess)

    return int(guess)


def desired_accuracy_reached(input, guess):
    tolerance = 0.000001
    return abs(input - guess**2) <= tolerance


def newton_raphson(input, guess):
    result = 1/2 * (guess + (input / guess))

    return result


print(square_root(49))
# 7
print(square_root(0))
# 0
print(square_root(-1))
# Please provide a number greater than zero
print(square_root("hello"))
# Please provide a number greater than zero
