import data as info

def greaterThan(users): 
    newArray = []

    for user in users:
        if user['age'] > 25:
            newArray.append(user)
    
    return newArray

print(greaterThan(info.data1)) 
print(greaterThan(info.data2)) 
print(greaterThan(info.data3)) 