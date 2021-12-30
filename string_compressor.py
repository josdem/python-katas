import itertools

def compress(keyword):
    result = ""
    for k,v in itertools.groupby(keyword, lambda n: keyword.count(n)):
        result = result + list(v)[0] + str(k)
    return result