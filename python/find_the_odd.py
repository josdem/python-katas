def find_it(array):
    return list(filter(lambda n: array.count(n) % 2, array))[0]