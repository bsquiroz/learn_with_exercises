def operartionsCond(num1, num2):
    add = num1 + num2

    if add > 20: return num1 / num2
    if add > 15: return num1 * num2
    if add > 10: return num1 - num2
    return add

print(operartionsCond(10, 20)) # 0.5
print(operartionsCond(1, 2)) # 3
print(operartionsCond(10, 7)) # 70
print(operartionsCond(3, 10)) # -7