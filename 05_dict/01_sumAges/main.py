import data as info

def sumAges(users): 
    sum = 0

    for user in users:
        sum += user['age']
    
    return sum
