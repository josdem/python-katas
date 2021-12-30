vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 'p', 'q', 's', 't', 'v', 'w','x', 'y', 'z']

def countVowels(keyword):
    return len([x for x in keyword if x in vowels])

def countConsonants(keyword):
    return len([x for x in keyword if x in consonants])
   