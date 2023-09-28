def amountVocals(phrase): 
    phrase = phrase.lower()
    amount = 0

    for char in phrase:
        if char in 'aeiou':
            amount += 1
    
    return amount


