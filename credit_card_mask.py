def maskify(credit_card):
    SUFFIX_LENGTH = 4
    if len(credit_card) <= SUFFIX_LENGTH:
      return credit_card
    else:
      return "#" * (len(credit_card) - SUFFIX_LENGTH) + credit_card[-SUFFIX_LENGTH:]