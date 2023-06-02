from unittest import result


def adder(numbers):
    result = []
    numbersAsString = [str(n) for n in numbers]
    for item in numbersAsString:
        result.append(sum([int(n) for n in list(item)]))
    return result