import data as info

def sumAges(users): 
    countHobbies = {}

    for user in users:
        for hobbie in user['hobbies']:
            
            if hobbie in countHobbies:
                countHobbies[hobbie] += 1
            else:
                countHobbies[hobbie] = 1

    return countHobbies

print(sumAges(info.data1)) 
print(sumAges(info.data2)) 
print(sumAges(info.data3)) 
