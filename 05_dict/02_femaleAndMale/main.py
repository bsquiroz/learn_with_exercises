import data as info

def femaleAndMale(users): 
    genderUsers = {
        'female': [],
        'male': []
    }

    for user in users:
        genderUsers['female'].append(user) if user['gender'] == 'female' else genderUsers['male'].append(user)
    
    return genderUsers
            
print(femaleAndMale(info.data1))
print(femaleAndMale(info.data2))
print(femaleAndMale(info.data3))