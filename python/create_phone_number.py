from python.array_diff import array_diff

def create_phone_number(array):
    string = ''.join(str(n) for n in array)
    return f'({string[:3]}) {string[3:6]}-{string[6:]}'
