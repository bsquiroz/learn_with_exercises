def totalMultiples(number, totalMultiples): 
    count = 1
    multiples = []

    while count <= totalMultiples:
        count += 1
        multiples.append(count * number)
    
    return multiples