import itertools

def find(numbers):
    for k, v in itertools.groupby(numbers, lambda n: numbers.count(n)):
        if(k == 1):
            return list(v)[0]