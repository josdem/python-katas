def compute(amount, keyboards, usbs):
    pairs = []
    for k in keyboards:
        for u in usbs:
            pairs.append((k, u))
    print(*pairs)        
    return amount + len(keyboards) + len(usbs)
