import re

pattern = '-?[0-9]+.?[0-9]+'

def biggest(data):
    return float(max([n for n in data if re.match(pattern, n)]))