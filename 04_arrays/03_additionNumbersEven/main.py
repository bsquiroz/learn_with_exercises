def addtionNumbersEven(numbers): 
    sum = 0

    for num in numbers: 
        if not num % 2:
            sum +=  num
    
    return sum