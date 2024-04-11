def count(string):
    return sum(1 for c in string if c.isupper())