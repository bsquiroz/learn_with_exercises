import data as info

def arrayToDict(users): 
    arrUsers = []

    for user in users:
        dictUser = {}

        for info in user:
            key, value = info.split('->')
            dictUser[key] = value
        
        arrUsers.append(dictUser)
    
    return arrUsers

print(arrayToDict(info.data1), '\n') # 96
print(arrayToDict(info.data2), '\n') # 135
print(arrayToDict(info.data3), '\n') # 101