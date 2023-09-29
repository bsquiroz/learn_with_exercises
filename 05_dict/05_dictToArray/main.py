import data as info

def dictToArray(users): 
    newArray = []

    for user in users:
        arrayValues = []
        
        for values in user:
            arrayValues.append(f'{values} -> {user[values]}')

        newArray.append(arrayValues)
    
    return newArray

print(dictToArray(info.data1), '\n') # 96
print(dictToArray(info.data2), '\n') # 135
print(dictToArray(info.data3), '\n') # 101