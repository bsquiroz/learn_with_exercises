def tableOfNumber(number): 
    table = ''

    for n in range(1, 10 + 1):
        result = n * number
        table += f'{result}-'

    return table[0:-1]

