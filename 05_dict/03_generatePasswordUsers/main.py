import data as info

def generatePasswordUsers(users): 

    for user in users:
        user['password'] = user['name'] + str(user['id'])
    
    return users
            
print(generatePasswordUsers(info.data1), '\n')
print(generatePasswordUsers(info.data2), '\n')
print(generatePasswordUsers(info.data3), '\n')