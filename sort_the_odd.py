def sort_array(array):
    odds = sorted((n for n in array if n % 2 == 1), reverse=True)
    return [n if n % 2 == 0 else odds.pop() for n in array]