def compute(amount, keyboards, usbs):
    pairs = []
    for k in keyboards:
        for u in usbs:
            pairs.append((k, u))
    prices = [p[0] + p[1] for p in pairs]
    return max([i for i in prices if i <= amount])
