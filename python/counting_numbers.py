def counter(numbers):
    return [len([x for x in numbers if x > 0]), len([x for x in numbers if x < 0]), len([x for x in numbers if x == 0])]