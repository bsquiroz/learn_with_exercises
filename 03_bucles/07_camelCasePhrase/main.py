def camelCasePhrase(phrase): 
    phrase = phrase.lower().split(' ')

    result = [phrase[0]]

    for i in range(1, len(phrase)):
        result.append(phrase[i].capitalize())
    
    return ''.join(result)


