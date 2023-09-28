def lowerUpperLower(phrase): 
    phrase = phrase.lower()
    result = ''

    for i in range(0, len(phrase)):
        if i % 2:
            result += phrase[i].upper()
        else: 
            result += phrase[i].lower()
    
    return result

