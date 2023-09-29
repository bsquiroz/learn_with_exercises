import data as info

def countPriority(tasks): 
    tasks_dict = {}

    for task in tasks:
        priority = task['priority']
        if priority in tasks_dict:
            tasks_dict[priority] += 1
        else: 
            tasks_dict[priority] = 1
    
    return tasks_dict

print(countPriority(info.data1)) # {'A': 3, 'B': 1, 'C': 3}
print(countPriority(info.data2)) # {'a': 2, 'c': 3, 'b': 2}
print(countPriority(info.data3)) # {'alta': 3, 'baja': 3, 'media': 1}