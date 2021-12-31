import itertools

def find(numbers):
    max = 0
    bigger = numbers[0]
    for k, v in itertools.groupby(numbers, lambda n: numbers.count(n)):
        if(k > max):
            max = k
            bigger = list(v)[0]
    return bigger