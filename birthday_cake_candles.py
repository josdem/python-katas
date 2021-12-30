def counter(candles):
    return list(filter(lambda it: it == max(candles), candles))