def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    array = list(string)
    result = [ch for ch in array if ch not in vowels]
    return ''.join(result)