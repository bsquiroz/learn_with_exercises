def amountVocals(phrase): 
    phrase = phrase.lower()
    result = ''

    for char in phrase:
        if char in 'aeiou':
            result += char
        elif char == ' ':
            result += ' '
        else:
            result += '_'
    
    return result


print(amountVocals('Esta sera una gran historia')) # e__a _e_a u_a __a_ _i__o_ia
print(amountVocals('Hola mundo desde RIWI')) # _o_a _u__o _e__e _i_i
print(amountVocals('Esto apenas comienza, esto no para')) # e__o a_e_a_ _o_ie__a_ e__o _o _a_a

