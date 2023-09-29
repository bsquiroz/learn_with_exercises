def listWordLen(phrase): 
    phrase = phrase.split(' ')

    result = []

    for word in phrase:
        result.append([word, len(word)])
    
    return result

