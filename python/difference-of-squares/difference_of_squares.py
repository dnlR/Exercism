def square_of_sum(count):
    return sum(range(1, count + 1)) ** 2


def sum_of_squares(count):
    return sum([n ** 2 for n in range(1, count + 1)])


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)