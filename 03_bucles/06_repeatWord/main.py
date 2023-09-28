def repeatWord(phrase): 
    phrase = phrase.split(' ')

    result = ''

    for word in phrase:
        result += f'{word}-{word}-'
    
    return result[0:-1]