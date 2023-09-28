def twoWords(phrase): 
    phrase = ''.join(phrase.split(' '))

    wordEven = ''
    wordOdd = ''

    for i in range(0, len(phrase)):
        if i % 2:
            wordOdd += phrase[i] 
        else:
           wordEven += phrase[i]
    
    return f'{wordEven} y {wordOdd}'