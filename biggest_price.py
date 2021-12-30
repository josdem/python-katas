import re

pattern = '-?[0-9]+.?[0-9]+'

def biggest(data):
    return float(max([l for l in data if re.match(pattern, l)]))
