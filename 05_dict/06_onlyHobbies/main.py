import data as info

def onlyHobbies(users): 
    newArray = []

    for user in users:
        for hobbie in user['hobbies']:
            if hobbie not in newArray:
                newArray.append(hobbie)
    
    return newArray

print(onlyHobbies(info.data1)) # 96
print(onlyHobbies(info.data2)) # 135
print(onlyHobbies(info.data3)) # 101