from python.array_diff import array_diff


def find_it(array):
    return list(filter(lambda n: array.count(n) % 2, array))[0]