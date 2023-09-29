def searchMultiples(num, limit): 
    multiples = []

    for i in range(1, limit + 2):
        res = num * i
        if not res % 2: multiples.append(res)
    
    return multiples