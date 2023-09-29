def sortedByLen(names): 
    return [
        sorted(names, key=len), sorted(names, key=len, reverse=True)
    ]
